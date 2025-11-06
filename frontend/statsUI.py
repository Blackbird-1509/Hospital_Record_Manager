from PySide6.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap


class window(QWidget):
    
    def __init__(self):
        super().__init__()

        self.counter = 1
        
        self.image_view = QLabel()

        self.image_set(self.counter)
        

        self.back = QPushButton("Back")
        if self.counter == 1:
            self.back.setDisabled(True)
        self.next = QPushButton("Next")
        self.back.clicked.connect(self.on_back_click)
        self.next.clicked.connect(self.on_next_click)
        

        
        inner_layout = QHBoxLayout()
        inner_layout.addWidget(self.back)
        inner_layout.addWidget(self.next)
        layout = QVBoxLayout()
        layout.addLayout(inner_layout)
        layout.addWidget(self.image_view)
        self.setLayout(layout)

    def on_next_click(self):
        if self.counter ==2:
            self.next.setDisabled(True)
        self.counter+=1
        self.image_set(self.counter)
        if self.counter >1:
            self.back.setDisabled(False)
    def on_back_click(self):
        self.counter-=1
        if self.counter<3:
            self.next.setDisabled(False)
        self.image_set(self.counter)
        if self.counter ==1:
            self.back.setDisabled(True)
    def image_set(self, counter):
        self.image = QPixmap(f"output{counter}.jpg")
        self.image_view.setPixmap(self.image)



