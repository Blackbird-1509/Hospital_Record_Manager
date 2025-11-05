from PySide6.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
import sys

app = QApplication([])

image_view = QLabel()
image = QPixmap("C:/Users/User/Pictures/FINAL TIMETABLE.jpg")
image_view.setPixmap(image)

class window(QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(image_view)
        self.setLayout(layout)

if __name__=="__main__":
    win = window()
    win.show()
    sys.exit(app.exec())
