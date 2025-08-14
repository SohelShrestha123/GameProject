import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class GameWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setUi()

    def setUi(self):
        self.setWindowTitle("Game")
        self.setGeometry(200, 200, 500, 350)

        lbl = QLabel(f"Welcome {self.username}")
        lbl.setFont(QFont("Times New Roman", 16))
        lbl.setAlignment(Qt.AlignCenter)

        continue_btn = QPushButton("Continue")
        continue_btn.setFont(QFont("Times New Roman", 12))
        continue_btn.setFixedSize(120, 40)

        l = QVBoxLayout()
        l.addWidget(lbl, alignment=Qt.AlignCenter)
        l.addSpacing(5)
        l.addWidget(continue_btn, alignment=Qt.AlignCenter)

        logout_btn = QPushButton("Logout")
        logout_btn.setFont(QFont("Arial", 10))
        logout_btn.setFixedSize(90, 28)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(logout_btn)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addLayout(l)
        layout.addStretch()
        layout.addLayout(bottom_layout)

        self.setLayout(layout)

    def logout(self):
        from login import LoginPage
        self.login = LoginPage()
        self.login.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow("Sohel")
    window.show()
    sys.exit(app.exec_())
