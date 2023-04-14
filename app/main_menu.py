import sys
import forms.home_page as home_page

from PyQt5 import QtWidgets



class MainWindow(QtWidgets.QMainWindow, home_page.Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.greetings_label.setText(f'Nice to meet you, {self.username}')

