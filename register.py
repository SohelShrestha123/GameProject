import re
import sqlite3
import sys
import hashlib
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QFormLayout, QRadioButton, QButtonGroup,
                             QMessageBox,QTimeEdit,QDateEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()

    def setUi(self):
        #For window
        self.setWindowTitle("Register Account")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("images/r.jpg"))

        #For form
        form=QFormLayout()
        self.lbl=QLabel("Register Account")
        self.lbl.setObjectName("lbl")

        self.lbl1=QLabel("Firstname: ")
        self.txt1=QLineEdit(self)
        self.lbl2 = QLabel("Lastname: ")
        self.txt2 = QLineEdit(self)
        self.lbl3 = QLabel("Username: ")
        self.txt3 = QLineEdit(self)
        self.add=QLabel("Address: ")
        self.add_in=QLineEdit(self)
        self.lbl4=QLabel("Email: ")
        self.txt4=QLineEdit(self)
        self.lbl5 = QLabel("New Password: ")
        self.txt5 = QLineEdit(self)
        self.txt5.setEchoMode(QLineEdit.Password)
        self.lbl6 = QLabel("Confirm Password: ")
        self.txt6 = QLineEdit(self)
        self.txt6.setEchoMode(QLineEdit.Password)
        self.lbl7 = QLabel("Gender")
        self.radiobutton1 = QRadioButton("Male")
        self.radiobutton1.setChecked(False)
        self.radiobutton1.gender = "Male"
        self.radiobutton2 = QRadioButton("Female")
        self.radiobutton2.setChecked(False)
        self.radiobutton2.gender = "Female"
        self.lbl8= QLabel("DOB: ")
        self.txt8 = QDateEdit(self)
        self.birth_time=QLabel("Birth Time: ")
        self.time_in=QTimeEdit(self)
        self.btn = QPushButton("Submit")
        self.btn.clicked.connect(self.validation)
        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.radiobutton1)
        self.btn_group.addButton(self.radiobutton2)

        self.loglbl = QLabel("<a href='login.py'>Login</a>")
        self.loglbl.setOpenExternalLinks(False)
        self.loglbl.linkActivated.connect(self.open_log)
        self.loglbl.setObjectName("loglbl")

        self.lbl.setAlignment(Qt.AlignHCenter)
        self.loglbl.setAlignment(Qt.AlignHCenter)

        form.addRow(self.lbl)
        form.addRow(self.lbl1, self.txt1)
        form.addRow(self.lbl2, self.txt2)
        form.addRow(self.lbl3, self.txt3)
        form.addRow(self.add,self.add_in)
        form.addRow(self.lbl4, self.txt4)
        form.addRow(self.lbl5, self.txt5)
        form.addRow(self.lbl6, self.txt6)
        form.addRow(self.lbl7)
        form.addRow(self.radiobutton1,self.radiobutton2 )
        form.addRow(self.lbl8,self.txt8)
        form.addRow(self.birth_time,self.time_in)
        form.addRow(self.btn)
        form.addRow(self.loglbl)

        self.setStyleSheet('''
               QLabel#lbl{
               font-size:30px;
               font-weight:bold;
               font-family:Times New Roman;
               margin:5px;
               }

               QLabel{
               font-size:18px;
               font-weight:bold;
               font-family:Times New Roman;
               margin:5px;
               }

               QRadioButton{
               font-size:16px;
               font-family:Times New Roman;
               }

               QLineEdit{
               font-size:16px;
               font-family:Times New Roman;
               }

               QLabel#loglbl{
               font-size:16px;
               font-family:Times New Roman;
               color:green;
               margin:5px;
               }

               QPushButton{
               font-size:20px;
               font-family:Times New Roman;
               background-color:#025222;
               color:white;
               border-radius:6px;
               padding:5px;
               margin:5px;
               }

               QPushButton::hover{
               color:#c784db;
               background-color:#2ff538;
               }
               ''')

        self.setLayout(form)

    def validation(self):
        fname=self.txt1.text().strip()
        lname=self.txt2.text().strip()
        uname=self.txt3.text().strip()
        a=self.add_in.text().strip()
        e=self.txt4.text().strip()
        np=self.txt5.text().strip()
        cp=self.txt6.text().strip()
        select=self.btn_group.checkedButton()
        dob=self.txt8.text().strip()
        b=self.time_in.text().strip()

        if not fname:
            self.display_error("First name is empty.")
            return

        if not lname:
            self.display_error("Last name is empty.")
            return

        if not uname:
            self.display_error("User name is empty.")
            return

        if not a:
            self.display_error("Address is empty.")
            return

        if not e:
            self.display_error("Email is empty.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", e):
            self.display_error("Invalid email format.")
            return

        if not np:
            self.display_error("New Password is empty.")
            return

        if not cp:
            self.display_error("Confirm Password is empty.")
            return

        if np != cp:
            self.display_error("Password didn't match.")
            return

        if select is None:
            self.display_error("Please select a gender.")
            return

        if not dob:
            self.display_error("Date on birth is empty.")
            return

        if not b:
            self.display_error("Birth Time is empty.")
            return

        gender = select.text()

        hashed_pw = hashlib.sha256(np.encode()).hexdigest()
        hashed_cp = hashlib.sha256(cp.encode()).hexdigest()

        con = sqlite3.connect('game.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM player WHERE username=? OR email=?", (uname, e))

        if cursor.fetchone():
            self.display_error("Username or email already exists.")
            return


        cursor.execute('''INSERT INTO player(firstname,lastname,username,address,email,newpassword,confirmpassword,gender,dob,birthtime)
        VALUES(?,?,?,?,?,?,?,?,?,?)''', (fname, lname, uname,a,e,hashed_pw,hashed_cp, gender,dob,b))
        con.commit()
        con.close()
        QMessageBox.information(self, "Account Created", "Your account has been created successfully.")
        self.clear_box()

        from character import CharacterCard
        self.char_card = CharacterCard(username=uname)
        self.char_card.show()
        self.close()

    def display_error(self, m):
        QMessageBox.critical(self, "Error", m)

    def clear_box(self):
        self.txt1.clear()
        self.txt2.clear()
        self.txt3.clear()
        self.add_in.clear()
        self.txt4.clear()
        self.txt5.clear()
        self.txt6.clear()
        self.txt8.clear()
        self.time_in.clear()

    def open_log(self):
        from login import LoginPage
        self.login=LoginPage()
        self.login.show()
        self.close()

if __name__ == "__main__":
    a = QApplication(sys.argv)
    w = RegisterPage()
    w.show()
    sys.exit(a.exec_())








