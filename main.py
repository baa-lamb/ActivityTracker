import os
import sys

from PySide6 import QtCore, QtWidgets

import constants
from dialogs.activityCreator import  ActivityCreatorDialog

## Main widget. Contains:
##      1) button to add new activity
##      2) list of current activities
class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.add_activity_button = QtWidgets.QPushButton("Add activity to track!")
        self.add_activity_button.setMinimumHeight(30)
        #self.add_activity_button.setStyleSheet()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.add_activity_button, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
        self.layout.setContentsMargins(3, 3, 0, 10)

        self.add_activity_button.clicked.connect(self.add_activity)

    ## add new activity dialog
    @QtCore.Slot()
    def add_activity(self):
        dialog = ActivityCreatorDialog()
        #dialog.resize(100, 80)
        dialog.exec()
        n = dialog.activity_name
        a = n


def main():
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.resize(constants.MAIN_WINDOW_W, constants.MAIN_WINDOW_H)
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()