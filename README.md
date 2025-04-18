# Task Manager + Pomodoro Timer

## Overview
The **Task Manager + Pomodoro Timer** is a productivity desktop application that combines task organization with the Pomodoro Technique. Users can manage to-do items and boost focus using a built-in timer that supports standard Pomodoro intervals. The app features a clean, responsive interface built using Python's PySide6 framework, and supports dark/light themes with a single click.

## Features
- ✅ **Task Management:** Add tasks with a simple UI.
- 🕒 **Pomodoro Timer:** 25-minute focus sessions with pause/resume/reset functionality.
- 🌗 **Theme Toggle:** Switch between dark and light mode in real time.
- 📋 **Dynamic UI:** All updates reflect immediately without reloading the app.
- 🧠 **Keyboard-Friendly:** Minimal mouse interaction required.

## Technologies Used
- **Python 3.12+:** Core programming language for the logic.
- **PySide6:** Used to build the graphical user interface (Qt for Python).
- **QTimer:** Handles countdown and real-time updates.
- **QWidgets, QVBoxLayout, QLabel, QPushButton, QListWidget, QLineEdit:** Core GUI components.

## Installation

1. Ensure you have **Python 3.12+** installed.

2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-manager-pomodoro.git
   ```
   
3. Navigate to the project folder:
   ```bash
   cd task-manager-pomodoro
   ```
   
4. (Recommended) Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the app:
   ```bash
   python main.py
   ```

## Project Preview

- **Dark mode:**
![dark_mode_app_python](https://github.com/user-attachments/assets/9fb8a94a-70d0-45c3-8a9e-47bf019b4c16)

- **Light mode:**
![light_mode_app_python](https://github.com/user-attachments/assets/b3b7b8b6-041a-45b4-a1a9-dbde0dcc8f45)

## Future Improvements

- Persistent task storage using JSON or SQLite.
- Task editing and deletion.
- Pomodoro break and long-break cycles.
- Daily stats and progress tracking.
