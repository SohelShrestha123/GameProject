import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class CharacterCard(QWidget):
    def __init__(self, username=None):
        super().__init__()
        self.username = username
        self.setWindowTitle("Character Profile")
        self.setStyleSheet("background-color: #6bd7ed;")
        self.setGeometry(200, 100, 500, 400)
        self.setUi()

    def get_player_data(self):
        con = sqlite3.connect("game.db")
        cursor = con.cursor()

        if self.username:
            cursor.execute("SELECT firstname, lastname, username, gender, dob FROM player WHERE username=?", (self.username,))
        else:
            cursor.execute("SELECT firstname, lastname, username, gender, dob FROM player LIMIT 1")

        row = cursor.fetchone()
        con.close()

        if row:
            return {
                "firstname": row[0],
                "lastname": row[1],
                "username": row[2],
                "gender": row[3],
                "dob": row[4]
            }
        else:
            return None

    def setUi(self):
        player = self.get_player_data()

        top = QHBoxLayout()

        img = QLabel()
        pic = QPixmap("images/samurai.png")
        pic = pic.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img.setPixmap(pic)
        img.setAlignment(Qt.AlignCenter)

        if player:
            info_text = (
                f"Name: {player['firstname']} {player['lastname']}\n"
                f"Username: {player['username']}\n"
                f"Gender: {player['gender']}\n"
                f"DOB: {player['dob']}\n"
                f"Job: Samurai\n"
                f"Class: Apprentice"
            )
        else:
            info_text = "No player data found."

        info = QLabel(info_text)
        info.setStyleSheet("color:#5e6263;")
        info.setFont(QFont("Times New Roman", 14))

        top.addWidget(img)
        top.addWidget(info)

        status = QLabel(
            "Stats:\n"
            "Health: 300/300\n"
            "Mana: 300/300\n"
            "Stamina: 150/150\n"
            "Luck: ★★★★★"
        )
        status.setStyleSheet("color:#5e6263;")
        status.setFont(QFont("Times New Roman", 14))
        status.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        main = QVBoxLayout()
        main.addLayout(top)
        main.addSpacing(20)
        main.addWidget(status)

        self.setLayout(main)


if __name__ == "__main__":
    a= QApplication(sys.argv)
    w = CharacterCard()
    w.show()
    sys.exit(a.exec_())