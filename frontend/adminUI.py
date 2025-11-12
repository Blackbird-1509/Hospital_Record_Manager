from PySide6.QtWidgets import QWidget, QPushButton, QTableWidget, QVBoxLayout, QTableWidgetItem, QHBoxLayout, QLabel, QComboBox, QLineEdit, QGridLayout
from PySide6.QtCore import Qt

import backend.admin as adminfunction
import frontend.statsUI as statsUI
import backend.stats as stats

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
        stats = QPushButton("Stats")
        stats.clicked.connect(self.on_stats_click)
        
        inner_layout = QHBoxLayout()
        inner_layout.addWidget(update)
        inner_layout.addWidget(delete)
        inner_layout.addWidget(refresh)
        inner_layout.addWidget(stats)

        layout = QVBoxLayout()
        layout.addLayout(inner_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.setFixedSize(840,500)

    def on_update_click(self):
        self.update = UpdateWin()
        self.update.show()

    def on_delete_click(self):
        self.delete = DeleteWin()
        self.delete.show()

    def refresher(self):
        self.table.clearContents()
        self.df = adminfunction.print_Op()
        self.headers = self.df.columns.astype(str)
        self.table.setRowCount(self.df.shape[0])
        for row_index, row_data in self.df.iterrows():
            for col_index, value in enumerate(row_data):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(value)))

    def on_stats_click(self):
        stats.stats_calculate()
        self.stat = statsUI.window()
        self.stat.show()
        self.close()


class UpdateWin (QWidget):
    def __init__(self):
        super().__init__()

        adminfunction.connect_Op()
        filter_list = ['Name', 'Age', 'Gender', 'DOB', 'Height', 'Weight', 'Blood_type' ]
        
        base = QLabel("Choose what to update")
        self.choice = QComboBox(placeholderText="Filter:")
        self.choice.addItems(filter_list)
        self.choice.currentTextChanged.connect(self.activate_filter)
        self.top = QLabel("<font color = grey>Choose id to update:</font>")
        self.id_up = QLineEdit(placeholderText="id")
        self.id_up.setEnabled(False)
        self.change = QLineEdit(placeholderText="Value")
        self.change_text = QLabel("<font coler = grey>Enter valid value</font>")
        self.change.setEnabled(False)
        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.cancel)
        self.updateBtn = QPushButton("Update")
        self.updateBtn.clicked.connect(self.update)

        self.layout = QGridLayout()
        self.layout.addWidget(base,0,0)
        self.layout.addWidget(self.choice,0,1)
        self.layout.addWidget(self.top,1,0)
        self.layout.addWidget(self.id_up,1,1)
        self.layout.addWidget(self.change_text,2,0)
        self.layout.addWidget(self.change, 2,1)
        self.layout.addWidget(self.cancelBtn, 3,0)
        self.layout.addWidget(self.updateBtn, 3,1)
        self.outer_layout = QVBoxLayout()
        self.outer_layout.addLayout(self.layout)

        self.setLayout(self.outer_layout)
    
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
        check = adminfunction.update_Op((choice, value, id))
        if check == 0:
            self.close()
        else:
            self.error = QLabel("<font color = red>Error</font>")
            self.outer_layout.addWidget(self.error, alignment=Qt.AlignmentFlag.AlignCenter)
    

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

        self.layout = QGridLayout()
        self.layout.addWidget(base,0,0)
        self.layout.addWidget(self.id_del,0,1)
        self.layout.addWidget(cancel, 1,0)
        self.layout.addWidget(delete,1,1)

        self.outer_layout = QVBoxLayout()
        self.outer_layout.addLayout(self.layout)

        self.setLayout(self.outer_layout)        

    def delete(self):
        id = int(self.id_del.text())
        check = adminfunction.del_Op(id)
        if check == 0:
            self.close()
        else:
            self.error = QLabel("<font color = red>Error</font>")
            self.outer_layout.addWidget(self.error, alignment=Qt.AlignmentFlag.AlignCenter)