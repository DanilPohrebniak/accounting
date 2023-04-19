import sys
import forms.home_page as home_page

from PyQt5 import QtWidgets
from app.reference import ReferencesPage



class MainWindow(QtWidgets.QMainWindow, home_page.Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.username = username
        self.greetings_label.setText(f'Nice to meet you, {self.username}')
        self.pressing_reference_tables()

    def pressing_reference_tables(self):
        self.reference.clicked.connect(lambda: self.open_reference_tables())

    def open_reference_tables(self):
        self.reference_pages = ReferencesPage()
        self.close()
        self.reference_pages.show()
