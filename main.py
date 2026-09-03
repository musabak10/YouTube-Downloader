import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp
import os
import threading

KAYIT_KLASORU = r"C:\Users\Pc\Desktop\Videolar\YouTube"


class YoutubeIndiriciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video İndirici")
        self.root.geometry("480x260")
        self.root.resizable(False, False)

        self.secenekler = []  # (etiket, format_string) listesi
        self.video_bilgisi_yuklendi = False

        # --- Link girişi ---
        tk.Label(root, text="YouTube Linki:").pack(anchor="w", padx=15, pady=(15, 0))

        link_frame = tk.Frame(root)
        link_frame.pack(fill="x", padx=15)

        self.link_entry = tk.Entry(link_frame)
        self.link_entry.pack(side="left", fill="x", expand=True)

        self.kontrol_btn = tk.Button(link_frame, text="Kontrol Et", command=self.formatlari_kontrol_et)
        self.kontrol_btn.pack(side="left", padx=(8, 0))

        # --- Kalite seçimi ---
        tk.Label(root, text="Kalite:").pack(anchor="w", padx=15, pady=(15, 0))

        self.kalite_combo = ttk.Combobox(root, state="disabled")
        self.kalite_combo.pack(fill="x", padx=15)

        # --- İndir butonu ---
        self.indir_btn = tk.Button(root, text="İndir", command=self.indirmeyi_baslat, state="disabled")
        self.indir_btn.pack(pady=15)

        # --- İlerleme çubuğu ---
        self.progress = ttk.Progressbar(root, orient="horizontal", length=430, mode="determinate")
        self.progress.pack(padx=15)

        # --- Durum yazısı ---
        self.durum_label = tk.Label(root, text="Bir link girip 'Kontrol Et' butonuna bas.", fg="gray")
        self.durum_label.pack(pady=(10, 0))

    # ---------- Formatları kontrol et ----------
    def formatlari_kontrol_et(self):
        url = self.link_entry.get().strip()
        if not url:
            messagebox.showwarning("Uyarı", "Lütfen bir link gir.")
            return

        self.durum_label.config(text="Video bilgisi alınıyor...", fg="blue")
        self.kontrol_btn.config(state="disabled")

        # UI donmasın diye ayrı thread'de çalıştır
        threading.Thread(target=self._formatlari_getir, args=(url,), daemon=True).start()

    def _formatlari_getir(self, url):
        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                formats = info.get('formats', [])

            gorulen = set()
            yukseklikler = []
            for f in formats:
                yukseklik = f.get('height')
                if yukseklik and f.get('vcodec') != 'none' and yukseklik not in gorulen:
                    gorulen.add(yukseklik)
                    yukseklikler.append(yukseklik)

            yukseklikler.sort(reverse=True)

            self.secenekler = [
                ("En iyi kalite (otomatik)", "bv*+ba[format_note*=original]/bv*+ba/b")
            ]
            for y in yukseklikler:
                self.secenekler.append((
                    f"{y}p",
                    f"bv*[height<={y}]+ba[format_note*=original]"
                    f"/bv*[height<={y}]+ba/b[height<={y}]"
                ))

            self.baslik = info.get('title', 'video')

            # GUI güncellemesi ana thread'de yapılmalı
            self.root.after(0, self._formatlari_guncelle)

        except Exception as e:
            self.root.after(0, lambda: self._hata_goster(f"Video bilgisi alınamadı:\n{e}"))

    def _formatlari_guncelle(self):
        etiketler = [s[0] for s in self.secenekler]
        self.kalite_combo['values'] = etiketler
        self.kalite_combo.current(0)
        self.kalite_combo.config(state="readonly")
        self.indir_btn.config(state="normal")
        self.kontrol_btn.config(state="normal")
        self.durum_label.config(text=f"Bulundu: {self.baslik}", fg="green")

    def _hata_goster(self, mesaj):
        self.kontrol_btn.config(state="normal")
        self.durum_label.config(text="Hata oluştu.", fg="red")
        messagebox.showerror("Hata", mesaj)

    # ---------- İndirme ----------
    def indirmeyi_baslat(self):
        url = self.link_entry.get().strip()
        secim_index = self.kalite_combo.current()

        if secim_index == -1:
            messagebox.showwarning("Uyarı", "Lütfen bir kalite seç.")
            return

        format_str = self.secenekler[secim_index][1]

        self.indir_btn.config(state="disabled")
        self.kontrol_btn.config(state="disabled")
        self.progress['value'] = 0
        self.durum_label.config(text="İndirme başlıyor...", fg="blue")

        threading.Thread(target=self._indir, args=(url, format_str), daemon=True).start()

    def _progress_hook(self, d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            indirilen = d.get('downloaded_bytes', 0)
            if total:
                yuzde = indirilen / total * 100
                hiz = d.get('speed')
                hiz_mb = f"{hiz / 1024 / 1024:.2f} MB/s" if hiz else ""
                self.root.after(0, lambda: self._progress_guncelle(yuzde, hiz_mb))
        elif d['status'] == 'finished':
            self.root.after(0, lambda: self.durum_label.config(text="Birleştiriliyor / işleniyor...", fg="blue"))

    def _progress_guncelle(self, yuzde, hiz_mb):
        self.progress['value'] = yuzde
        self.durum_label.config(text=f"İndiriliyor... %{yuzde:.1f}  {hiz_mb}", fg="blue")

    def _indir(self, url, format_str):
        try:
            os.makedirs(KAYIT_KLASORU, exist_ok=True)

            options = {
                "format": format_str,
                "merge_output_format": "mp4",
                "outtmpl": os.path.join(KAYIT_KLASORU, "%(title)s.%(ext)s"),
                "progress_hooks": [self._progress_hook],
            }

            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])

            self.root.after(0, self._indirme_tamamlandi)

        except Exception as e:
            self.root.after(0, lambda: self._hata_goster(f"İndirme başarısız:\n{e}"))
            self.root.after(0, self._butonlari_ac)

    def _indirme_tamamlandi(self):
        self.progress['value'] = 100
        self.durum_label.config(text="İndirme tamamlandı! ✅", fg="green")
        self._butonlari_ac()
        messagebox.showinfo("Tamamlandı", f"Video indirildi:\n{KAYIT_KLASORU}")

    def _butonlari_ac(self):
        self.indir_btn.config(state="normal")
        self.kontrol_btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = YoutubeIndiriciApp(root)
    root.mainloop()
