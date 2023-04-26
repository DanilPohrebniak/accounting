import sys
import forms.reference as references_page

from PyQt5 import QtWidgets
from app.reference_tables_form import ReferencesShow



class ReferencesPage(QtWidgets.QMainWindow, references_page.Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.login = login
        self.username.setText(login)
        self.selected_reference = ''
        self.pressing_units()
        self.pressing_warehouse()
        self.pressing_counterparty()
        self.pressing_goods()
        self.pressing_logout()


    def pressing_warehouse(self):
        self.warehouse.clicked.connect(lambda: self.open_warehouse())

    def pressing_units(self):
        self.units.clicked.connect(lambda: self.open_units())

    def pressing_counterparty(self):
        self.counterparty.clicked.connect(lambda: self.open_counterparty())

    def pressing_goods(self):
        self.goods.clicked.connect(lambda: self.open_goods())

    def pressing_logout(self):
        self.logout.clicked.connect(lambda: self.open_login_form())

    def open_login_form(self):
        import main as login_form
        self.main_window = login_form.App()
        self.close()
        self.main_window.show()

    def open_warehouse(self):
        self.open('Warehouse')

    def open_units(self):
        self.open('Units')

    def open_counterparty(self):
        self.open('Counterparty')

    def open_goods(self):
        self.open('Goods')

    def open(self, selected_reference):
        self.selected_reference = selected_reference
        self.main_window = ReferencesShow(self.selected_reference, self.login)
        self.close()
        self.main_window.show()