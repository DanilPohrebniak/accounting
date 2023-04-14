import sys
import forms.home_page as home_page

from PyQt5 import QtWidgets



class MainWindow(QtWidgets.QMainWindow, home_page.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
