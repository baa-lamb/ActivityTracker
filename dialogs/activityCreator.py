from PySide6 import QtCore, QtWidgets, QtGui

## Dialog to create new activity
class ActivityCreatorDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        super().setWindowTitle("Add new activity")

        self.activity_name = ""

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Activity")
        self.ok_button = QtWidgets.QPushButton("apply")
        self.cancel_button = QtWidgets.QPushButton("cancel")

        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.line_edit, 0, 0, 1, 2, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.ok_button, 1, 0, 1, 1, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.cancel_button, 1, 1, 1, 1, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        layout.setContentsMargins(3, 3, 1, 1)

        self.ok_button.clicked.connect(self.set_activity_name)
        self.cancel_button.clicked.connect(self.reject)

    def set_activity_name(self):
        self.activity_name = self.line_edit.text()
        if self.activity_name == "":
            message_box = QtWidgets.QMessageBox(self)
            message_box.setText("Enter activity name!")
            message_box.exec()
        else:

            self.accept()