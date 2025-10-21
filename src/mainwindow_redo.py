from PySide6 import QtWidgets 
from PySide6.QtWidgets import QMainWindow, QTableWidget
from PySide6 import QtGui
from PySide6 import QtCore
# Import the custom class created with QtDesigner
from ui_mainwindow_redo import Ui_MainWindow

class FUSEWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Cloudfuse')

        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)

        self.tableView.setSpan(1,1,3,3)
        self.tableView.showRow(1)