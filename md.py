import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from views.addBook import Ui_AddBookWindow

class MainWindow(QMainWindow, Ui_AddBookWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Connect close button
        self.close_btn.clicked.connect(self.close)
        
        # Connect cancel button
        self.cancel_btn.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
