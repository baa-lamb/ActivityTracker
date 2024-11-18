import os
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Start Here!")
        self.text = QtWidgets.QLabel(self.hello[0], alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


def main():
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.resize(400, 600)
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()