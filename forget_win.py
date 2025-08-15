import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QFormLayout, QLineEdit, QPushButton, QMessageBox, QWidget, QLabel


class ForgotPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Forgot Password")
        self.setGeometry(300, 200, 350, 250)

        l = QFormLayout()
        self.username=QLabel("Enter Username: ")
        self.username_input = QLineEdit()

        self.new_password=QLabel("Enter new password: ")
        self.new_pass_input = QLineEdit()

        self.confirm_password=QLabel("Enter Confirm Password: ")
        self.confirm_pass_input = QLineEdit()
        self.confirm_pass_input.setEchoMode(QLineEdit.Password)

        self.reset_btn = QPushButton("Reset Password")
        self.reset_btn.clicked.connect(self.reset_password)

        l.addRow(self.username,self.username_input)
        l.addRow(self.new_password, self.new_pass_input)
        l.addRow(self.confirm_password, self.confirm_pass_input)
        l.addRow(self.reset_btn)

        self.setLayout(l)

    def reset_password(self):
        username = self.username_input.text().strip()
        new_pass = self.new_pass_input.text().strip()
        confirm_pass = self.confirm_pass_input.text().strip()

        if not username or not new_pass or not confirm_pass:
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        if new_pass != confirm_pass:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return

        conn= sqlite3.connect('game.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM player WHERE username=?", (username,))
        user = cursor.fetchone()

        if user:
            cursor.execute("UPDATE player SET confirmpassword=? WHERE username=?", (new_pass, username))
            conn.commit()
            QMessageBox.information(self, "Success", "Password changed successfully.")
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Username not found.")

        conn.close()

if __name__ == "__main__":
    a = QApplication(sys.argv)
    w = ForgotPage()
    w.show()
    sys.exit(a.exec_())
