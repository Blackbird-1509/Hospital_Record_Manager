from PySide6.QtWidgets import QComboBox, QPushButton, QGridLayout, QWidget, QLineEdit, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator, QDoubleValidator

import backend.client as clientfunction

class window(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Patient Form")
        self.age_validator = QIntValidator(1,150)
        self.double_validator = QDoubleValidator(0, 500, 3)
       
        
        self.name_box = QLineEdit(placeholderText="Name")
        self.age_box = QLineEdit(placeholderText="Age")
        self.age_box.setValidator(self.age_validator)
        self.gender = QComboBox(placeholderText="Gender")
        self.gender.addItems(['M', 'F'])
        self.dob_box = QLineEdit(placeholderText="DOB: YYYY-MM-DD")
        self.height_ = QLineEdit(placeholderText="Height (in cm)")
        self.height_.setValidator(self.double_validator)
        self.weight = QLineEdit(placeholderText="Weight (in cm)")
        self.weight.setValidator(self.double_validator)
        self.blood_type = QComboBox(placeholderText="Blood Type")
        self.blood_type.addItems(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.confirm_clicked)

        heading = QLabel("Enter patient details")
        font = heading.font()
        font.setBold(True)
        font.setPointSize(18)
        heading.setFont(font)
        
        self.success = QLabel("")
        font.setPointSize(10)
        self.success.setFont(font)


        outer_layout = QVBoxLayout()
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

        outer_layout.addWidget(heading, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.name_box, 1,0)
        layout.addWidget(self.age_box, 1,1)
        layout.addWidget(self.gender, 1,2)
        layout.addWidget(self.dob_box, 1, 3)
        layout.addWidget(self.height_, 2, 0)
        layout.addWidget(self.weight, 2, 1)
        layout.addWidget(self.blood_type, 2,2)
        layout.addWidget(self.confirm_button, 2,3)

        outer_layout.addLayout(layout)
        outer_layout.addWidget(self.success, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(outer_layout)

    def confirm_clicked(self):
        clientfunction.connect_Op()
        name = self.name_box.text()
        age = int(self.age_box.text())
        gender = self.gender.currentText()
        dob = self.dob_box.text()
        height = float(self.height_.text())
        weight = float(self.weight.text())
        blood = self.blood_type.currentText()
        result = clientfunction.insert_Op((name, age, gender, dob, height, weight, blood))
        if result == 0:
            self.success.setText("Successfully Added")
        else:
            self.success.setText("Error adding values. Please retry")


        
