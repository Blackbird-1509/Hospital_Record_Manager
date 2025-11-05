from PySide6.QtWidgets import QWidget, QPushButton, QTableWidget, QVBoxLayout, QTableWidgetItem, QHBoxLayout, QLabel, QComboBox, QLineEdit, QGridLayout
import backend.admin as adminfunction

class window(QWidget):
    def __init__(self):
        super().__init__()

        adminfunction.connect_Op()
        self.row, self.col = adminfunction.count_Op()
        

        self.table = QTableWidget(rowCount=self.row, columnCount=self.col)
        self.refresher()
        self.table.setHorizontalHeaderLabels(self.headers)
        self.table.verticalHeader().setVisible(False)
        
        update = QPushButton("Update")
        update.clicked.connect(self.on_update_click)
        delete = QPushButton("Delete")
        delete.clicked.connect(self.on_delete_click)
        refresh = QPushButton("Refresh")
        refresh.clicked.connect(self.refresher)
        
        inner_layout = QHBoxLayout()
        inner_layout.addWidget(update)
        inner_layout.addWidget(delete)
        inner_layout.addWidget(refresh)
        layout = QVBoxLayout()
        layout.addLayout(inner_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.setFixedSize(770,500)

    def on_update_click(self):
        self.update = UpdateWin()
        self.update.show()

    def on_delete_click(self):
        self.delete = DeleteWin()
        self.delete.show()

    def refresher(self):
         self.table.clearContents()
         self.data, self.headers = adminfunction.print_Op()
         self.table.setRowCount(len(self.data))
         for r, row in enumerate(self.data):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(val)))
         

            
class UpdateWin (QWidget):
    def __init__(self):
        super().__init__()

        adminfunction.connect_Op()
        filter_list = ['Name', 'Age', 'Gender', 'DOB', 'Height', 'Weight', 'Blood_type' ]
        
        base = QLabel("Choose what to update")
        self.choice = QComboBox(placeholderText="Filter:")
        self.choice.addItems(filter_list)
        self.top = QLabel("<font color = grey>Choose id to update:</font>")
        self.id_up = QLineEdit(placeholderText="id")
        self.id_up.setEnabled(False)
        self.change = QLineEdit(placeholderText="Value")
        self.change_text = QLabel("<font coler = grey>Enter valid value</font>")
        self.change.setEnabled(False)
        self.choice.currentTextChanged.connect(self.activate_filter)
        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.cancel)
        self.updateBtn = QPushButton("Update")
        self.updateBtn.clicked.connect(self.update)


        layout = QGridLayout()
        layout.addWidget(base,0,0)
        layout.addWidget(self.choice,0,1)
        layout.addWidget(self.top,1,0)
        layout.addWidget(self.id_up,1,1)
        layout.addWidget(self.change_text,2,0)
        layout.addWidget(self.change, 2,1)
        layout.addWidget(self.cancelBtn, 3,0)
        layout.addWidget(self.updateBtn, 3,1)
        


        self.setLayout(layout)
    
    def activate_filter(self):
            self.top.setText("Choose id to update:")
            self.id_up.setEnabled(True)
            self.change_text.setText("Enter valid value")
            self.change.setEnabled(True)
    def cancel(self):
         self.close()
    def update(self):
        choice = self.choice.currentText()
        value = self.change.text()
        id = int(self.id_up.text())
        print((choice, value, id))
        

        adminfunction.update_Op((choice, value, id))
    

class DeleteWin(QWidget):
    def __init__(self):
        super().__init__()
        base = QLabel("Select id to delete")
        self.id_del = QLineEdit(placeholderText="id")
        cancel = QPushButton("Cancel")
        delete = QPushButton("Delete")
        obj = UpdateWin()
        delete.clicked.connect(self.delete)
        cancel.clicked.connect(obj.cancel)



        layout = QGridLayout()
        layout.addWidget(base,0,0)
        layout.addWidget(self.id_del,0,1)
        layout.addWidget(cancel, 1,0)
        layout.addWidget(delete,1,1)

        self.setLayout(layout)

    def delete(self):
        id = int(self.id_del.text())
        adminfunction.del_Op(id)




