import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QListWidget, QHBoxLayout, QLineEdit, QLabel, QMessageBox
)
from PySide6.QtCore import QTimer


class PomodoroApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager + Pomodoro")
        self.setGeometry(100, 100, 400, 400)

        # Theme setup
        self.dark_mode = True
        self.light_theme = """
            QWidget {
                background-color: #ffffff;
                color: #000000;
                font-family: Arial;
            }
            QPushButton {
                background-color: #dddddd;
                color: #000000;
                border-radius: 5px;
                padding: 5px;
            }
            QLineEdit, QListWidget {
                background-color: #f2f2f2;
                color: #000000;
            }
        """
        self.dark_theme = """
            QWidget {
                background-color: #1e1e1e;
                color: #f0f0f0;
                font-family: Arial;
            }
            QPushButton {
                background-color: #3a3a3a;
                color: #f0f0f0;
                border-radius: 5px;
                padding: 5px;
            }
            QLineEdit, QListWidget {
                background-color: #2e2e2e;
                color: #f0f0f0;
            }
        """

        self.init_ui()
        self.apply_theme()

        # Timer settings
        self.pomodoro_duration = 25 * 60  # 25 minutes in seconds
        self.time_left = self.pomodoro_duration
        self.timer_running = False

    def init_ui(self):
        layout = QVBoxLayout()

        # Task input layout (text field + add button)
        task_input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.add_task)

        task_input_layout.addWidget(self.task_input)
        task_input_layout.addWidget(self.add_task_button)

        # Task list widget
        self.task_list = QListWidget()

        # Pomodoro timer settings
        self.timer_label = QLabel("25:00")
        self.timer_label.setStyleSheet("font-size: 32px;")
        self.start_timer_button = QPushButton("Start Pomodoro")
        self.start_timer_button.clicked.connect(self.toggle_timer)

        # Theme toggle button
        self.theme_toggle_button = QPushButton("Switch to Light Mode")
        self.theme_toggle_button.clicked.connect(self.toggle_theme)

        # QTimer for the countdown
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1 second
        self.timer.timeout.connect(self.update_timer)

        # Add all widgets to the main layout
        layout.addLayout(task_input_layout)
        layout.addWidget(self.task_list)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.start_timer_button)
        layout.addWidget(self.theme_toggle_button)

        self.setLayout(layout)

    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet(self.dark_theme)
        else:
            self.setStyleSheet(self.light_theme)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()
        if self.dark_mode:
            self.theme_toggle_button.setText("Switch to Light Mode")
        else:
            self.theme_toggle_button.setText("Switch to Dark Mode")

    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Task cannot be empty.")

    def toggle_timer(self):
        if not self.timer_running:
            self.timer.start()
            self.start_timer_button.setText("Pause Pomodoro")
            self.timer_running = True
        else:
            self.timer.stop()
            self.start_timer_button.setText("Resume Pomodoro")
            self.timer_running = False

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer_label()
        else:
            self.timer.stop()
            self.timer_running = False
            self.start_timer_button.setText("Start Pomodoro")
            QMessageBox.information(
                self, "Pomodoro Finished", "Time for a break!")
            self.reset_timer()

    def update_timer_label(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.setText(f"{minutes:02}:{seconds:02}")

    def reset_timer(self):
        self.time_left = self.pomodoro_duration
        self.update_timer_label()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec())