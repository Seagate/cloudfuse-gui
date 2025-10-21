from PySide6.QtWidgets import (
    QApplication, QWidget, QTableView, QVBoxLayout, QPushButton, QStyledItemDelegate, 
    QStyleOptionButton, QStyle, QMessageBox,QHeaderView
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QModelIndex, QRect
import sys

class ButtonDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if index.column() == 2:
            button = QStyleOptionButton()
            button.rect = option.rect
            button.text = "Click"
            button.state = QStyle.State_Enabled
            QApplication.style().drawControl(QStyle.CE_PushButton, button, painter)
        else:
            super().paint(painter, option, index)

    def editorEvent(self, event, model, option, index):
        if index.column() == 2 and event.type() == event.MouseButtonRelease:
            day = model.index(index.row(), 0).data()
            person = model.index(index.row(), 1).data()
            QMessageBox.information(None, "Button Clicked", f"{day} - {person}")
            return True
        return super().editorEvent(event, model, option, index)

class TableViewDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3x3 Table with Buttons")
        self.resize(400, 200)

        layout = QVBoxLayout(self)
        self.table = QTableView()
        layout.addWidget(self.table)

        self.model = QStandardItemModel(3, 3)
        self.model.setHorizontalHeaderLabels(["Day", "Person", "Action"])

        data = [
            ["Monday", "Alice"],
            ["Tuesday", "Bob"],
            ["Wednesday", "Charlie"]
        ]

        for row, (day, person) in enumerate(data):
            self.model.setItem(row, 0, QStandardItem(day))
            self.model.setItem(row, 1, QStandardItem(person))
            self.model.setItem(row, 2, QStandardItem(""))  # Placeholder for button
        self.table.setModel(self.model)
        self.table.setItemDelegate(ButtonDelegate())
        
        # Stretch all columns to fill the window width
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = TableViewDemo()
    demo.show()
    sys.exit(app.exec())