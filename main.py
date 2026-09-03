import yt_dlp
import os

def formatlari_listele(url):
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
    
    
    gorulen = set()
    secenekler = []
    for f in formats:
        yukseklik = f.get('height')
        if yukseklik and f.get('vcodec') != 'none' and yukseklik not in gorulen:
            gorulen.add(yukseklik)
            secenekler.append(yukseklik)
    
    secenekler.sort(reverse=True)
    return secenekler, info.get('title', 'video')

def video_indir(url, secilen_kalite):
    kayit_klasoru = r"C:\Users\Pc\Desktop\Videolar\YouTube"
    os.makedirs(kayit_klasoru, exist_ok=True)

    if secilen_kalite == "en iyi":
        format_str = "bv*+ba/b"
    else:
        
        format_str = f"bv*[height<={secilen_kalite}]+ba/b[height<={secilen_kalite}]"

    options = {
        "format": format_str,
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(kayit_klasoru, "%(title)s.%(ext)s"),
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    print("İndirme tamamlandı!")

if __name__ == "__main__":
    url = input("YouTube linkini gir: ")

    print("Formatlar kontrol ediliyor...")
    secenekler, baslik = formatlari_listele(url)

    print(f"\nVideo: {baslik}")
    print("Mevcut kaliteler:")
    for i, s in enumerate(secenekler, 1):
        print(f"{i}. {s}p")
    print(f"{len(secenekler)+1}. En iyi kalite (otomatik)")

    secim = input("\nHangi kaliteyi istersin? (numara gir): ")
    secim = int(secim)

    if secim == len(secenekler) + 1:
        video_indir(url, "en iyi")
    else:
        video_indir(url, secenekler[secim - 1])
