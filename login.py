import sqlite3
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,QMessageBox,
                             QPushButton,QFormLayout)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setGeometry(200,200,350,450)

        login_format=QFormLayout()
        self.lbl=QLabel("Login Your Account")

        self.img=QLabel()
        self.img.setFixedSize(100,100)
        self.img.setAlignment(Qt.AlignCenter)
        self.pic=QPixmap("images/p.png")
        pic = self.pic.scaled(self.img.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img.setPixmap(pic)
        self.lbl1=QLabel("Username: ")
        self.user_input=QLineEdit(self)
        self.lbl2=QLabel("Password: ")
        self.pass_input=QLineEdit(self)
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.forget=QLabel("<a href='#'>Forget Password?</a>")
        self.forget.setOpenExternalLinks(False)
        self.forget.linkActivated.connect(self.open_forgot)
        self.forget.setAlignment(Qt.AlignCenter)
        self.log_btn=QPushButton("Login")
        self.log_btn.clicked.connect(self.log_acc)
        self.lbl3 = QLabel("Create an account?")
        self.lbl4 = QLabel("<a href='register_page.py'>Register</a>")
        self.lbl4.setOpenExternalLinks(False)
        self.lbl4.linkActivated.connect(self.open_reg)
        self.lbl3.setObjectName("lbl3")
        self.lbl4.setObjectName("lbl4")
        self.lbl.setObjectName("lbl")

        login_format.addRow(self.lbl)
        login_format.addRow(self.img)
        login_format.addRow(self.lbl1)
        login_format.addRow(self.user_input)
        login_format.addRow(self.lbl2)
        login_format.addRow(self.pass_input)
        login_format.addRow(self.forget)
        login_format.addRow(self.log_btn)
        login_format.addRow(self.lbl3, self.lbl4)

        login_format.setAlignment(self.img,Qt.AlignCenter)

        self.lbl.setAlignment(Qt.AlignHCenter)
        self.lbl1.setAlignment(Qt.AlignHCenter)
        self.user_input.setAlignment(Qt.AlignHCenter)
        self.lbl2.setAlignment(Qt.AlignHCenter)
        self.pass_input.setAlignment(Qt.AlignHCenter)

        self.setStyleSheet("""
               QPushButton{
               font-family:Times New Roman;
               font-size:20px;
               font-weight:bold;
               background-color:#79f7f7;
               border-radius:5px;
               color:#f67dfa;
               padding:10px;
               }

               QPushButton::hover{
                background-color:#5fd6fa;
                color: white;
               }

               QLabel{
                font-family:Times New Roman;
                font-size:20px;
                font-weight:bold;
               }

               QLabel#lbl3{
                font-family:Times New Roman;
                font-size:18px;
                font-weight:bold;
                padding:10px;
               }

               QLabel#lbl4{
                font-family:Times New Roman;
                font-size:16px;
                color:red;
               }

               QLabel#lbl{
               font-weight:bold;
               font-family:Times New Roman;
               font-size:30px;
               }

               QLineEdit{
               font-family:Times New Roman;
                font-size:20px;
                margin:4px;
                padding:4px;
               }

               QLabel#i{
               margin:1px;
               }

               """)

        self.setLayout(login_format)

    def log_acc(self):
            username = self.user_input.text().strip()
            password = self.pass_input.text().strip()

            if not username or not password:
                QMessageBox.warning(self, "Error", "Please enter both email and password.")
                return

            con = sqlite3.connect('game.db')
            cursor = con.cursor()
            cursor.execute("SELECT * FROM player WHERE username=? AND confirmpassword=?", (username, password))
            u = cursor.fetchone()
            con.close()
            if u:
                from gamewindow import GameWindow
                self.game = GameWindow(username)
                self.game.show()
                self.close()

            else:
                QMessageBox.critical(self, "Error", "Invalid email or password.")

           

    def open_forgot(self):
        from forget_win import ForgotPage
        self.forget_win = ForgotPage()
        self.forget_win.show()
        self.close()

    def open_reg(self):
        from register import RegisterPage
        self.register = RegisterPage()
        self.register.show()
        self.close()

if __name__ == "__main__":
    a = QApplication(sys.argv)
    w = LoginPage()
    w.show()
    sys.exit(a.exec_())








