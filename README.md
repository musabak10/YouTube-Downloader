# 🎬 YouTube Video Downloader

A simple and user-friendly **YouTube Video Downloader** built with Python.

This project uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) to retrieve available video formats and provides a graphical user interface where users can select their preferred video quality and download the video.

The application is built with **Tkinter** and includes real-time download progress and download speed monitoring.

---

## ✨ Features

* 🖥️ **Graphical User Interface (GUI)**
* 🔗 YouTube URL input
* 🔍 Automatic video format detection
* 🎞️ Automatic resolution detection
* 🎯 Quality selection
* ⭐ **Best Quality** download option
* 📊 Real-time download progress bar
* ⚡ Real-time download speed display
* 🧵 Background processing with `threading`
* 🎵 Automatic video and audio merging
* 🎬 MP4 output
* 📁 Automatic download directory creation
* 🔄 Duplicate resolution filtering
* ⚠️ User-friendly error messages
* 🚀 Non-blocking GUI during downloads

---

## 🖼️ How It Works

```text
             YouTube URL
                  │
                  ▼
           🔍 Check Video
                  │
                  ▼
        Retrieve Video Formats
                  │
                  ▼
       Detect Available Qualities
                  │
                  ▼
          🎞️ Select Quality
                  │
                  ▼
              ⬇️ Download
                  │
                  ▼
       📊 Show Download Progress
                  │
                  ▼
       🎵 Merge Video + Audio
                  │
                  ▼
              🎬 MP4 File
```

---

## 🛠️ Technologies

| Technology   | Purpose                           |
| ------------ | --------------------------------- |
| 🐍 Python    | Main programming language         |
| 🎨 Tkinter   | Graphical user interface          |
| 🎬 yt-dlp    | Video information and downloading |
| 🧵 Threading | Background processing             |
| 📁 os        | File and directory management     |
| 🎛️ ttk      | GUI components and progress bar   |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/musabak10/YouTube-Video-Downloader.git
```

### 2. Navigate to the Project Directory

```bash
cd YouTube-Video-Downloader
```

### 3. Install Dependencies

Install the required Python package:

```bash
pip install -r requirements.txt
```

Or install `yt-dlp` directly:

```bash
pip install yt-dlp
```

---

## ⚙️ FFmpeg

**FFmpeg** is required when video and audio streams need to be merged.

For example, high-quality YouTube formats may provide the video and audio as separate streams. `yt-dlp` downloads these streams separately and FFmpeg combines them into a single MP4 file.

Make sure FFmpeg is installed and available in your system `PATH`.

---

## 🚀 Usage

Run the application:

```bash
python main.py
```

### 1. 🔗 Enter a YouTube URL

Paste the YouTube video URL into the URL input field.

### 2. 🔍 Check the Video

Click the **Check Video** button.

The application will:

* Retrieve the video information
* Analyze available formats
* Detect available resolutions
* Remove duplicate resolutions
* Display the available quality options

### 3. 🎞️ Select a Quality

Available options may look like:

```text
Best Quality (Automatic)
1080p
720p
480p
360p
144p
```

### 4. ⬇️ Start the Download

Select your preferred quality and click the **Download** button.

During the download, the application displays:

```text
Downloading... 64.7%   5.32 MB/s
```

This provides real-time information about the download progress and current download speed.

### 5. ✅ Download Completed

When the download is finished, the application displays a completion message and saves the video to the configured output directory.

---

## 📊 Real-Time Download Progress

The application uses `yt-dlp`'s **progress hooks** to monitor the download process.

The interface can display:

* 📈 Download percentage
* ⚡ Current download speed
* 🔄 Processing/merging status
* ✅ Completion status

> **Note:** The displayed speed is the current download throughput while downloading the video. It is not a measurement of your internet connection's maximum speed.

---

## 🧵 Multithreading

Downloading a video or retrieving video information can take some time.

To prevent the GUI from becoming unresponsive, the application uses Python's `threading` module.

For example:

```python
threading.Thread(...)
```

Background threads are used for time-consuming operations while GUI updates are safely performed through Tkinter's main thread.

This allows the application to:

* Keep the interface responsive
* Update the progress bar
* Display download speed
* Process downloads without freezing the window

---

## 🎞️ Automatic Quality Detection

The application retrieves the available formats using `yt-dlp`.

Video formats are filtered using the video codec information:

```python
if yukseklik and f.get('vcodec') != 'none':
```

The program then uses a Python `set` to prevent duplicate resolutions:

```python
gorulen = set()
```

For example, if multiple formats contain the same resolution, the user will only see:

```text
1080p
720p
480p
360p
```

instead of seeing the same resolution multiple times.

---

## ⭐ Best Quality Mode

The application provides a **Best Quality** option:

```text
Best Quality (Automatic)
```

This allows `yt-dlp` to automatically select the best available video and audio combination.

The format selection is handled using:

```python
bv*+ba/b
```

---

## 📁 Output Directory

Downloaded videos are saved to:

```text
Desktop/
└── Videolar/
    └── YouTube/
```

The application automatically creates the directory if it does not already exist.

---

## 🔧 Project Structure

```text
YouTube-Video-Downloader/
│
├── main.py
├── requirements.txt
├── README.md
└── ...
```

---

## 🔄 Project Evolution

The first version of this project was a **terminal-based YouTube downloader**.

### Previous Version

The original version:

* Used the terminal interface
* Required users to enter a quality number
* Displayed information directly in the console
* Had limited download progress feedback

### 🚀 Current Version

The project has been upgraded into a graphical desktop application.

The new version introduces:

* 🖥️ Tkinter GUI
* 🔍 Automatic format detection
* 🎞️ Graphical quality selection
* 📊 Real-time progress bar
* ⚡ Download speed monitoring
* 🧵 Multithreading
* ⚠️ GUI-based error handling
* 🎵 Automatic video/audio merging
* ⭐ Best-quality mode

This transformation makes the project more user-friendly and demonstrates the transition from a simple command-line script to a more structured desktop application.

---

## 💡 Concepts Practiced

This project provides practical experience with several Python concepts:

* Object-Oriented Programming
* Classes and Objects
* Tkinter GUI Development
* Event-driven programming
* Multithreading
* Exception Handling
* Lists and Sets
* File and Directory Management
* External Python Libraries
* Progress Callbacks
* Video and Audio Processing
* Format Selection
* Background Task Management

---

## 📋 Requirements

The project requires:

* Python 3.x
* `yt-dlp`
* FFmpeg

Python dependencies are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Disclaimer

This project was created for **educational and personal development purposes**.

Users are responsible for complying with YouTube's Terms of Service, copyright laws, and the rights of content creators.

Only download content that you have permission or legal rights to download.

---

## 👨‍💻 Author

**Musab Akten**

Computer Engineering Student

GitHub:
https://github.com/musabak10

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ **Star** on GitHub.

More features and improvements may be added in future versions.
