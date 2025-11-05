from PySide6.QtWidgets import QComboBox, QPushButton, QGridLayout, QWidget, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator, QDoubleValidator

import backend.client as clientfunction

class window(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Patient Form")
        self.age_validator = QIntValidator(1,150)
        self.double_validator = QDoubleValidator(0, 500, 3)
       
        
        name_box = QLineEdit(placeholderText="Name")
        age_box = QLineEdit(placeholderText="Age")
        age_box.setValidator(self.age_validator)
        gender = QComboBox(placeholderText="Gender")
        gender.addItems(['M', 'F'])
        dob_box = QLineEdit(placeholderText="DOB: YYYY-MM-DD")
        height = QLineEdit(placeholderText="Height (in cm)")
        height.setValidator(self.double_validator)
        weight = QLineEdit(placeholderText="Weight (in cm)")
        weight.setValidator(self.double_validator)
        blood_type = QComboBox(placeholderText="Blood Type")
        blood_type.addItems(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        confirm_button = QPushButton("Confirm")

        heading = QLabel("Enter patient details")
        font = heading.font()
        font.setBold(True)
        font.setPointSize(18)
        heading.setFont(font)


        layout = QGridLayout()
        layout.setSpacing(50)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setColumnStretch(1,1)
        layout.setColumnStretch(0,1)
        layout.setColumnStretch(2,1)
        layout.setRowStretch(1,1)
        layout.setRowStretch(0,1)
        layout.setRowStretch(2,1)
        layout.setRowStretch(3,1)


        

        self.setLayout(layout)
        clientfunction.connect_Op()
