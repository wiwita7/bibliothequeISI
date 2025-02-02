from PySide6.QtWidgets import QApplication
from dash import Dashboard
from login import LoginWindow
from PySide6.QtGui import QIcon, QPixmap

import sys
# Run the application

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.setWindowTitle("Library Login")
    window.setWindowIcon(QIcon("../ressources/icons/uit-white.png"))
    window.show()

    sys.exit(app.exec())
