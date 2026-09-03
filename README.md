# 🎬 YouTube Video Downloader

A powerful and user-friendly **Python-based YouTube video downloader** built with [`yt-dlp`](https://github.com/yt-dlp/yt-dlp). The project provides an interactive command-line interface for retrieving available video resolutions, selecting the desired quality, and downloading the video with automatic audio/video stream merging.

The downloader is designed to keep the process simple while giving the user control over the output quality and download behavior.

---

## ✨ Features

* 🎥 **YouTube video downloading** using `yt-dlp`
* 📊 **Automatic format detection**
* 🎚️ **Interactive video quality selection**
* 🏆 **Best-quality automatic selection**
* 🔊 **Automatic video + audio stream merging**
* 📦 **MP4 output support**
* 📁 **Automatic download directory creation**
* 🔄 **Automatically selects the best available stream within the requested resolution**
* 🧹 **Prevents duplicate resolutions from appearing**
* 💻 **Simple command-line interface**
* ⚡ **Fast and efficient downloading**

---

## 🆕 What's New?

This version improves the original downloader by introducing a more structured and intelligent quality-selection system.

### 🔹 Dynamic Quality Detection

Instead of relying on predefined resolutions, the program analyzes the formats provided by YouTube and dynamically detects the available video resolutions.

For example:

```text
Available qualities:

1. 1080p
2. 720p
3. 480p
4. 360p
5. Best Quality (Automatic)
```

This means the available options automatically adapt to the video being downloaded.

### 🔹 Duplicate Resolution Filtering

The downloader uses Python's `set` data structure to prevent the same resolution from appearing multiple times.

For example, if YouTube provides multiple `1080p` video streams, the user will still see:

```text
1080p
```

only once.

### 🔹 Improved Quality Selection

The selected resolution is now treated as a **maximum resolution limit**.

For example, selecting:

```text
720p
```

allows `yt-dlp` to choose the best compatible video stream with a height of **720p or lower**, instead of requiring an exact format.

### 🔹 Automatic Video + Audio Merging

Many YouTube formats provide video and audio as separate streams.

The downloader automatically selects:

```text
Best Video + Best Audio
```

and merges them into a single MP4-compatible output.

This allows the program to obtain higher-quality video streams while still providing a complete video file with audio.

### 🔹 Best Quality Mode

The new version also includes an automatic option:

```text
Best Quality (Automatic)
```

When selected, the program lets `yt-dlp` determine the best available combination of video and audio streams.

---

## 🛠️ Technologies Used

| Technology | Purpose                              |
| ---------- | ------------------------------------ |
| 🐍 Python  | Core programming language            |
| ⚙️ yt-dlp  | Video extraction and downloading     |
| 📂 os      | Directory and file-system management |

---

## 🔄 How It Works

The application follows a simple workflow:

```text
        YouTube URL
             │
             ▼
    🔍 Extract Video Info
             │
             ▼
    📊 Detect Available Formats
             │
             ▼
    🧹 Remove Duplicate Resolutions
             │
             ▼
    🎚️ User Selects Quality
             │
             ▼
    🎥 Select Video Stream
             │
             ▼
    🔊 Select Audio Stream
             │
             ▼
    🔗 Merge Video + Audio
             │
             ▼
       📦 MP4 Output
```

---

## 📂 Output

Downloaded videos are automatically stored in:

```text
C:\Users\Pc\Desktop\Videolar\YouTube
```

If the directory does not exist, the program automatically creates it.

---

## 🚀 Installation

Install the required dependency:

```bash
pip install yt-dlp
```

Then run the Python script:

```bash
python youtube_downloader.py
```

---

## 💻 Example Usage

```text
YouTube linkini gir: https://www.youtube.com/...

Formatlar kontrol ediliyor...

Video: Example Video

Mevcut kaliteler:
1. 1080p
2. 720p
3. 480p
4. 360p
5. En iyi kalite (otomatik)

Hangi kaliteyi istersin? (numara gir): 2
```

The program then downloads the best compatible video/audio combination for the selected quality.

---

## 📌 Project Highlights

This project demonstrates practical usage of several Python concepts:

* Functions and modular program structure
* Lists and sets
* Loops and conditional statements
* String formatting
* Exception-aware file handling
* External Python libraries
* Command-line user interaction
* Dynamic data processing
* File-system operations
* Video/audio stream management

---

## ⚠️ Disclaimer

This project is intended for **educational and personal use**. Users are responsible for ensuring that their use of downloaded content complies with YouTube's Terms of Service and applicable copyright laws.

---

## 👨‍💻 Author

**Musab Akten**

Computer Engineering Student | Python & Software Development

---

⭐ If you find this project useful, consider giving the repository a star!
