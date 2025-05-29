# 🧠 MyCourseUI – Learn Your Own Courses Like Udemy

**MyCourseUI** is a React-based web application that turns any directory of video files on your computer into a course platform with a **Udemy-style interface**. Track your progress, navigate through chapters and lessons, and learn efficiently — all from your local files.

---

## 🎯 Purpose

If you have a collection of tutorials, bootcamp recordings, or video courses saved on your computer, this project lets you:

- 🎥 Watch them in a structured format (Course → Chapters → Lessons)
- ✅ Track your progress lesson by lesson
- 🧭 Resume from where you left off
- 💻 Use it completely offline, locally

---

## 📁 How It Works

1. **Organize your course folder** like this:

```
My Courses/
├── Course A/
│   ├── Chapter 1/
│   │   ├── 1. Introduction.mp4
│   │   └── 2. Setup.mov
│   └── Chapter 2/
│       └── 1. Advanced Topics.mkv
├── Course B/
│   └── ...
```

2. **Run a Python script** that scans your course directory and generates a JSON file (`courses-structured.json`) used by the React frontend.

3. The script also links (or copies) your course folder into `public/course/` so the React app can access your video files.

4. Launch the React app (`npm start`) and enjoy a Udemy-like experience!

---

## 🚀 Features

- 🧩 Automatic detection of course structure
- 📚 Organized by course → chapter → lesson
- ✅ Progress tracking saved locally (with reset option)
- 🔁 Resume from last watched video (auto-scroll)
- ⚡ Works 100% offline

---

## 📦 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/b3ng0x/MyCourseUI.git
cd mycourseui
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Prepare Your Courses

Put your courses in a folder like:

```bash
~/Videos/My-Courses/
```

Then update the Python script with this path.

### 4. Run the Python Script

```bash
python3 courses.py
```

It will:
- Generate `public/courses-structured.json`
- Link or copy your course folder to `public/course/`

### 5. Start the App

```bash
npm start
```

Open [http://localhost:3000](http://localhost:3000)

---

## 🛠 Tech Stack

- ⚛️ React
- 🎬 HTML5 Video Player
- 🐍 Python (for file parsing and linking)
- 💾 LocalStorage (for progress tracking)
