# Terminal ASCII Animation Maker 🎨🖥️

A lightweight, zero-dependency Python utility for creating, editing, and playing back frame-by-frame ASCII animations directly inside your command-line interface. 

Built using pure Python with zero external packages required!

---

## ✨ Features

- **Interactive Line-by-Line Editor:** Type your ASCII art frame by frame with instant line controls.
- **Frame Management:** View (`LIST`), modify (`EDIT <num>`), and delete (`DELETE` or `DELETE <num>`) specific frames easily.
- **Real-Time Playback:** Preview your animation at adjustable speeds (Frames Per Second).
- **Instant Stop:** Press **`q`** or **`ESC`** at any time during playback to jump right back into the editor.
- **Zero Scroll Clutter:** Utilizes terminal alternate screen buffers so your main terminal history stays completely clean.
- **Zero Dependencies:** Runs entirely on Python's standard library (`os`, `time`, `sys`, `msvcrt`).

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3** installed on your system. No extra libraries or `pip install` commands are needed!

### Running the Tool
1. Clone this repository or download `ascii_animator.py`:
   ```bash
git clone https://github.com/minhchau1504-svg/terminal-ascii-animator.git
cd terminal-ascii-animator
