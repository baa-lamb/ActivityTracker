import os
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


## Dialog to create new activity
class ActivityCreatorDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.activity_name = ""

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Activity")

        self.ok_button = QtWidgets.QPushButton("apply")
        self.ok_button.clicked.connect(self.set_activity_name)

        self.cancel_button = QtWidgets.QPushButton("cancel")
        self.cancel_button.clicked.connect(self.reject)

        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.line_edit, 0, 0, 2, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.ok_button, 1, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.cancel_button, 1, 1, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        #layout.setContentsMargins(10, 10, 10, 10)

    def set_activity_name(self):
        self.activity_name = self.line_edit.text()
        if self.activity_name == "":
            message_box = QtWidgets.QMessageBox(self)
            message_box.setText("Enter activity name!")
            message_box.exec_()
        else:
            self.accept()


## Main widget. Contains:
##      1) button to add new activity
##      2) list of current activities
class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.add_activity_button = QtWidgets.QPushButton("Add activity to track!")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.add_activity_button)

        self.add_activity_button.clicked.connect(self.add_activity)

    ## add new activity dialog
    @QtCore.Slot()
    def add_activity(self):
        dialog = ActivityCreatorDialog()
        #dialog.resize(100, 80)
        dialog.exec_()
        n = dialog.activity_name
        a = n


def main():
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.resize(300, 600)
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()