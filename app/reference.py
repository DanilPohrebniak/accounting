import sys
import forms.reference as references_page

from PyQt5 import QtWidgets
from app.reference_tables_form import ReferencesShow



class ReferencesPage(QtWidgets.QMainWindow, references_page.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.selected_reference = ''
        self.pressing_units()
        self.pressing_warehouse()
        self.pressing_counterparty()


    def pressing_warehouse(self):
        self.warehouse.clicked.connect(lambda: self.open_warehouse())

    def pressing_units(self):
        self.units.clicked.connect(lambda: self.open_units())

    def pressing_counterparty(self):
        self.counterparty.clicked.connect(lambda: self.open_counterparty())

    def open_warehouse(self):
        self.selected_reference = 'Warehouse'
        self.main_window = ReferencesShow(self.selected_reference)
        self.close()
        self.main_window.show()

    def open_units(self):
        self.selected_reference = 'Units'
        self.main_window = ReferencesShow(self.selected_reference)
        self.close()
        self.main_window.show()

    def open_counterparty(self):
        self.selected_reference = 'Counterparty'
        self.main_window = ReferencesShow(self.selected_reference)
        self.close()
        self.main_window.show()