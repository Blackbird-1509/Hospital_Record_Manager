from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

import backend.auth as auth
import frontend.adminUI as adminUI

class window(QWidget):
    def __init__(self):
        super().__init__()

        log = QLabel("Login")
        font = log.font()
        font.setPointSize(20)
        font.setBold(True)
        log.setFont(font)

        self.log_fail = QLabel("")
        font.setPointSize(10)
        self.log_fail.setFont(font)

        self.user = QLineEdit(placeholderText="Username")
        self.user.setFixedSize(300, 20)
        self.pass_w = QLineEdit(placeholderText="Password")
        self.pass_w.setEchoMode(QLineEdit.Password)
        self.pass_w.setFixedSize(300, 20)

        login = QPushButton("Login")
        login.clicked.connect(self.login_check)

        layout = QVBoxLayout()
        layout.addWidget(log, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.user, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.pass_w, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(login, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.log_fail, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(10)
        layout.setContentsMargins(0, 70, 0, 30)

        self.setLayout(layout)
        self.setFixedSize(500,500)



    def login_check(self):
        username = self.user.text()
        password = self.pass_w.text()
        check = auth.login_acc(username, password)
        self.log_fail.setText("Success")

        if check:
            self.admin = adminUI.window()
            self.admin.show()
            self.close()
        else:
            self.log_fail.setText("Incorrect username or password")
