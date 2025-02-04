# notification.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication
from PySide6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, Qt, QPoint

class NotificationWindow(QWidget):
    def __init__(self, message="Notification", timeout=3000, position=QPoint(100, 100)):
        super().__init__()

        # Set window properties
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(300, 80)  # ✅ Adjusted window size

        # Apply background styling
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 128, 220);  /* Dark blue */
                border-radius: 10px;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
        """)

        # Layout and Message Label
        layout = QVBoxLayout(self)
        self.message_label = QLabel(message, self)
        self.message_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.message_label)

        # Close Button
        self.close_btn = QPushButton("X", self)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: white;
                font-size: 14px;
                border: none;
            }
            QPushButton:hover {
                color: red;
            }
        """)
        self.close_btn.clicked.connect(self.close)
        layout.addWidget(self.close_btn, alignment=Qt.AlignRight)

        # ✅ Set the notification position to match the button
        self.move(position)

        # Fade-in Animation
        self.fade_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_animation.setDuration(500)
        self.fade_animation.setStartValue(0)
        self.fade_animation.setEndValue(1)
        self.fade_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.fade_animation.start()

        # Auto-close after timeout
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.fadeOut)
        self.timer.start(timeout)

    def fadeOut(self):
        """Fade-out animation before closing"""
        self.fade_animation.setDuration(500)
        self.fade_animation.setStartValue(1)
        self.fade_animation.setEndValue(0)
        self.fade_animation.finished.connect(self.close)
        self.fade_animation.start()
