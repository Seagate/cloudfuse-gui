from PySide6 import QtWidgets 
from PySide6.QtWidgets import QMainWindow, QTableWidget, QSizePolicy
from PySide6 import QtGui
from PySide6 import QtCore
import random
# Import the custom class created with QtDesigner
from ui_mainwindow_redo import Ui_MainWindow

class FUSEWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Cloudfuse')

        self.tableWidget.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Expanding)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Mount Name', 'Status'])
        self.tableWidget.show()

        self.pushButton_settings.setIcon(QtGui.QIcon(str("src/gear_icon.png")))
        self.pushButton_newMount.setIcon(QtGui.QIcon(str("src/add_icon.png")))
        self.pushButton_mountbuttton.setCheckable(True)
        self.pushButton_mountbuttton.setChecked(True)

        self.pushButton_mountbuttton.setStyleSheet("""
            QPushButton {
                background-color: white; /* Color when unchecked */
                border: clear;
            }
            QPushButton:checked {
                background-color: white; /* Color when checked */
            }
        """)        

        self.pushButton_mountbuttton.setIcon(QtGui.QIcon(str("src/play_icon.png")))
        self.pushButton_mountbuttton.clicked.connect(self.toggle_mount)
        self.pushButton_forget.setIcon(QtGui.QIcon(str("src/trash_icon.png")))
        self.pushButton_newMount.clicked.connect(self.add_mount)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.pushButton_forget.clicked.connect(self.forget_mount)

    def toggle_mount(self):
        if self.pushButton_mountbuttton.isChecked():
            self.pushButton_mountbuttton.setIcon(QtGui.QIcon(str("src/play_icon.png")))
        else:
            self.pushButton_mountbuttton.setIcon(QtGui.QIcon(str("src/pause_icon.png")))

 
    def add_mount(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        name = "Mount " + str(random.randint(1,100))

        item = QtWidgets.QTableWidgetItem()

        mountStatus = ['Mounted', 'Unmounted', 'Error', 'Warning']
        status = random.choice(mountStatus)
        
        item.setText(status)
        if status == 'Mounted':
            tablePixmap = QtGui.QPixmap("src/mounted_icon.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio)
        elif status == 'Unmounted':
            tablePixmap = QtGui.QPixmap("src/unmounted_icon.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio)
        elif status == 'Error':
            tablePixmap = QtGui.QPixmap("src/error_icon.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio)
        else:
            tablePixmap = QtGui.QPixmap("src/warning_icon.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio)

        tableIcon = QtGui.QIcon(tablePixmap)
        item.setIcon(tableIcon)

        self.tableWidget.setItem(rowPosition , 0 , QtWidgets.QTableWidgetItem(name))

        self.tableWidget.setItem(rowPosition , 1 , item)

        

    def cell_was_clicked(self):
        selectedRow = self.tableWidget.currentRow()
        status = self.tableWidget.item(selectedRow , 1).text()
        if status == 'Mounted':
            self.pushButton_mountbuttton.setChecked(True)
        elif status == 'Unmounted':
            self.pushButton_mountbuttton.setChecked(False)
        else:
            self.pushButton_mountbuttton.setChecked(False)
        self.pushButton_mountbuttton.clicked.emit()

    def forget_mount(self):
        selectedRow = self.tableWidget.currentRow()
        if selectedRow < 0:
            print("No row selected to forget")
            return
        self.tableWidget.removeRow(selectedRow)
        self.tableWidget.setCurrentItem(None)

for(x in range(3)):
    app = QtWidgets.QApplication([])
    window = FUSEWindow()
    window.show()
    app.exec()
