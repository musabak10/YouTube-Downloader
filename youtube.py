import yt_dlp
import os

os.makedirs(r"C:\Users\Pc\Desktop\Videolar\YouTube", exist_ok=True)
url = input("YouTube linkini gir: ")

options = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "outtmpl": r"C:\Users\Pc\Desktop\Videolar\YouTube\%(title)s.%(ext)s"
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

print("İndirme tamamlandı!")