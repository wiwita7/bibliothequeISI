from PySide6.QtWidgets import QApplication
from dash_view import DashboardWindow
from login import LoginWindow
from PySide6.QtGui import QIcon, QPixmap

from PySide6.QtCore import QTimer
# Run the application
from PySide6.QtWidgets import QApplication, QMainWindow
from views.notification import NotificationWindow  # Import the notification class
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UIT Library Dashboard")
        self.setGeometry(300, 100, 900, 600)

        # Example: Show notification when window opens
        QTimer.singleShot(1000, lambda: self.showNotification("Welcome to UIT Library!"))

    def showNotification(self, message="New Notification!"):
        """Creates and displays a floating notification"""
        self.notification = NotificationWindow(message)
        self.notification.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.setWindowTitle("Library UIT")
    window.setWindowIcon(QIcon("../ressources/icons/uit-white.png"))
    window.show()
    sys.exit(app.exec())
