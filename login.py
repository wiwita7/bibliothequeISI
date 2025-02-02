import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QPoint
from views.log import Ui_Form  # Import the auto-generated UI file
import time
from PySide6.QtCore import QTimer
from dash_view import MainWindow  # Import Dashboard


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()  # Initialize the UI
        self.ui.setupUi(self)
        # Set the username field text color to Blue Ranger
        self.ui.username.setStyleSheet("""
            background-color: white;
            padding: 5px;
            font-size: 14px;
            color: #051380;  /* Blue Ranger color */
        """)

        # Set the password field text color to Blue Ranger
        self.ui.password.setStyleSheet("""
            background-color: white;
            padding: 5px;
            font-size: 14px;
            color: #051380;  /* Blue Ranger color */
        """)
        # Set the same style for both "Connect" and "Cancel" buttons
        
        button_style = """
        QPushButton {
            background-color: rgb(0,0,128);
            color: rgb(255,255,255);
            border-radius: 5px;
            padding: 5px;
            transition: background-color 0.3s ease-in-out;

        }

        QPushButton:hover {
            background-color: rgb(85,105,255); /* Lighter blue on hover */
        }

        QPushButton:pressed {
        background-color: rgb(255,69,0); /* Smooth red on press */
        }
        """
        self.ui.pushButton.setStyleSheet(button_style)  # Apply to "Connect" button
        self.ui.pushButton_2.setStyleSheet(button_style)  # Apply the same style to "Cancel" button

        # Apply border-radius to labels
        label_style = """
        QLabel {
            border-radius: 10px;
            background-color: white;
        }
        """
        # Apply to all labels that need rounded corners
        self.ui.label.setStyleSheet(label_style)
        



        # Set the window to be frameless and transparent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Allow window dragging by tracking mouse events
        self.dragging = False
        self.offset = QPoint()
        self.ui.widget.mousePressEvent = self.mousePressEvent
        self.ui.widget.mouseMoveEvent = self.mouseMoveEvent
        self.ui.widget.mouseReleaseEvent = self.mouseReleaseEvent

        # Load the UIT logo with scaling
        self.ui.uitLogo.setPixmap(QPixmap("../ressources/icons/uit-white.png"))
        self.ui.uitLogo.setScaledContents(True)

        # Set placeholder texts for username and password fields
        self.ui.username.setPlaceholderText("Username")
        self.ui.password.setPlaceholderText("Password")

        # Set password field to hide input by default
        self.ui.password.setEchoMode(QLineEdit.Password)

        # Connect the toggle password visibility button
        self.ui.toggle_password.clicked.connect(self.toggle_password_visibility)

        # Connect buttons
        self.ui.pushButton.clicked.connect(self.check_login)
        self.ui.pushButton_2.clicked.connect(self.close)

    def mousePressEvent(self, event):
        """Track the mouse position for dragging."""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """Move the window while dragging."""
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.offset)
            event.accept()

    def mouseReleaseEvent(self, event):
        """Stop dragging."""
        self.dragging = False

    def toggle_password_visibility(self):
        """Toggle the password visibility between hidden and visible."""
        if self.ui.password.echoMode() == QLineEdit.Password:
            self.ui.password.setEchoMode(QLineEdit.Normal)
            self.ui.toggle_password.setIcon(QIcon("../ressources/icons/eye.png"))
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)
            self.ui.toggle_password.setIcon(QIcon("../ressources/icons/eye-slash.png"))


    def check_login(self):
        """Simulate login processing before opening dashboard."""
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please fill in both fields.")
            return

        # Disable buttons and show loading text
        self.ui.pushButton.setText("Connecting...")
        self.ui.pushButton.setEnabled(False)

        # Simulate loading (after 1 second, check credentials)
        QTimer.singleShot(1000, self.validate_login)

    def validate_login(self):
        """Final validation and opening dashboard."""
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()

        # Dummy check (Replace with real database authentication)
        if username == "admin" and password == "1234":
            #QMessageBox.information(self, "Success", "Login successful!")
            self.close()  # Close login window
            self.open_dashboard()
        else:
            QMessageBox.critical(self, "Error", "Invalid credentials. Try again.")
            self.ui.pushButton.setText("Connect")  # Reset button text
            self.ui.pushButton.setEnabled(True)  # Re-enable button


    def open_dashboard(self):
        """Open the dashboard window."""
        self.dashboard = MainWindow()  # Create an instance of the Dashboard class
        self.dashboard.show()  # Show the dashboard window
        self.close()  # Close the login window



