from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sys

# Fenêtre du Dashboard
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(200, 200, 400, 300)
        layout = QVBoxLayout()
        label = QLabel("Bienvenue sur le Dashboard!")
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)

# Fenêtre de Login
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 350, 200)
        
        layout = QVBoxLayout()
        
        self.label_username = QLabel("Nom d'utilisateur:")
        self.input_username = QLineEdit()
        
        self.label_password = QLabel("Mot de passe:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.button_login = QPushButton("Se connecter")
        self.button_cancel = QPushButton("Annuler")
        self.button_fingerprint = QPushButton("Empreinte digitale")
        
        self.button_login.clicked.connect(self.verify_login)
        self.button_cancel.clicked.connect(self.close)
        self.button_fingerprint.clicked.connect(self.fingerprint_authentication)
        
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_fingerprint)
        layout.addWidget(self.button_cancel)
        
        self.setLayout(layout)

    def verify_login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        
        if username == "admin" and password == "password123":
            self.open_dashboard()
        else:
            QMessageBox.warning(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect!")
    
    def fingerprint_authentication(self):
        # Simuler une authentification biométrique réussie
        QMessageBox.information(self, "Empreinte digitale", "Authentification réussie avec empreinte digitale!")
        self.open_dashboard()
        
    def open_dashboard(self):
        self.dashboard = Dashboard()
        self.dashboard.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
