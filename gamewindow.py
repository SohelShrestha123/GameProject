import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
)
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class GameWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.background=QPixmap("images/fantasy.jpg")
        self.setUi()

    def setUi(self):
        self.setWindowTitle("Game")
        self.setGeometry(200, 200, 500, 350)

        self.pal=QPalette()
        self.pal.setBrush(QPalette.Window,QBrush(self.background))
        self.setPalette(self.pal)

        self.lbl = QLabel(f"Welcome {self.username}")
        self.lbl.setFont(QFont("Times New Roman", 28))
        self.lbl.setAlignment(Qt.AlignCenter)

        self.continue_btn = QPushButton("Continue")
        self.continue_btn.setFont(QFont("Times New Roman", 12))
        self.continue_btn.setFixedSize(120, 40)


        self.l = QVBoxLayout()
        self.l.addWidget(self.lbl, alignment=Qt.AlignCenter)
        self.l.addSpacing(5)
        self.l.addWidget(self.continue_btn, alignment=Qt.AlignCenter)

        self.logout_btn = QPushButton("Logout")
        self.logout_btn.setFont(QFont("Times New Roman", 10))
        self.logout_btn.clicked.connect(self.logout)
        self.logout_btn.setFixedSize(90, 28)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addStretch()
        self.bottom_layout.addWidget(self.logout_btn)

        self.layout = QVBoxLayout()
        self.layout.addStretch()
        self.layout.addLayout(self.l)
        self.layout.addStretch()
        self.layout.addLayout(self.bottom_layout)

        self.setLayout(self.layout)

    def set_background(self):
        bg = QPixmap(self.background).scaled(
            self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
        )
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(bg))
        self.setPalette(palette)

    def resizeEvent(self, event):
        self.set_background()
        super().resizeEvent(event)

    def logout(self):
        from login import LoginPage
        self.login = LoginPage()
        self.login.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow("")
    window.show()
    sys.exit(app.exec_())
