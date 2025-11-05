from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QComboBox, QPushButton
from PySide6.QtCore import QSize, Qt, QMargins
import frontend.clientUI as clientUI
import frontend.adminUI as adminUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hospital Record Manager")
        self.setFixedSize(QSize(500,500))


        title = QLabel("Welcome to Hospital Record Manager")
        font = title.font()
        font.setPointSize(16)
        font.setBold(True)
        title.setFont(font)
        

        subtitle = QLabel("You are:")
        font = subtitle.font()
        font.setPointSize(10)
        font.setBold(True)
        subtitle.setFont(font)

        self.option = QComboBox()
        self.option.setFixedSize(300,20)
        self.option.addItems(["Patient", "Admin"])

        confirmButton = QPushButton()
        confirmButton.setBaseSize(40,40)
        confirmButton.setText("Confirm")
        confirmButton.clicked.connect(self.confirm_clicked)


        layout = QVBoxLayout()
        layout.setContentsMargins(QMargins(20,80,20,80))
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.option, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(confirmButton, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def confirm_clicked(self):
        text = self.option.currentText()
        if text == "Admin":
            self.adminWindow = adminUI.window()  
            self.adminWindow.show()
            self.hide()
        else:
            self.patientWindow = clientUI.window()
            self.patientWindow.show()
            self.hide()