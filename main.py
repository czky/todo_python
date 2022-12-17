# To-do application using PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "To-do"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.CreateLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        self.widget = QWidget()
        self.widget.setLayout(vbox)

        self.setCentralWidget(self.widget)

        self.show()

    def CreateLayout(self):
        self.groupbox = QGroupBox("To-do")
        self.groupbox.setFont(QFont("Consolas", 13))

        self.listwidget = QListWidget()

        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("Enter task")

        self.button = QPushButton("Add")
        self.button.clicked.connect(self.AddTask)

        self.button2 = QPushButton("Delete")
        self.button2.clicked.connect(self.DeleteTask)

        self.hboxlayout = QHBoxLayout()
        self.hboxlayout.addWidget(self.lineedit)
        self.hboxlayout.addWidget(self.button)
        self.hboxlayout.addWidget(self.button2)

        self.vboxlayout = QVBoxLayout()
        self.vboxlayout.addWidget(self.listwidget)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.groupbox.setLayout(self.vboxlayout)

    # add task
    def AddTask(self):
        task = self.lineedit.text()
        self.listwidget.addItem(task)
        self.lineedit.setText("")

    # delete task
    def DeleteTask(self):
        for selecteditem in self.listwidget.selectedItems():
            self.listwidget.takeItem(self.listwidget.row(selecteditem))

    # add task with enter
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.AddTask()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
