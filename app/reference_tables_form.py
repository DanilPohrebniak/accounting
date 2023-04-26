import sys
import forms.reference_tables_form as references_show
import utils.db_utils as db_utils

from PyQt5 import QtWidgets
from app.warehouse_create import WarehouseCreate
from app.units_create import UnitsCreate
from app.counterparty_create import CounterpartyCreate
from app.goods_create import GoodsCreate



class ReferencesShow(QtWidgets.QMainWindow, references_show.Ui_MainWindow):
    def __init__(self, reference, login):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.login = login
        self.username.setText(login)
        self.selected_reference = reference
        self.pressing_reference_tables()
        self.pressing_add()
        self.fill_data()
        self.pressing_delete()
        self.pressing_logout()

    def pressing_add(self):
        self.add.clicked.connect(lambda: self.open_reference())

    def pressing_reference_tables(self):
        self.reference.clicked.connect(lambda: self.open_reference_tables())

    def pressing_delete(self):
        self.delete_2.clicked.connect(lambda: self.delete_data())

    def pressing_logout(self):
        self.logout.clicked.connect(lambda: self.open_login_form())

    def open_login_form(self):
        import main as login_form
        self.main_window = login_form.App()
        self.close()
        self.main_window.show()

    def open_reference(self):
        if self.selected_reference == 'Warehouse':
            self.reference_window = WarehouseCreate(self.login)
        elif self.selected_reference == 'Units':
            self.reference_window = UnitsCreate(self.login)
        elif self.selected_reference == 'Counterparty':
            self.reference_window = CounterpartyCreate(self.login)
        elif self.selected_reference == 'Goods':
            self.reference_window = GoodsCreate(self.login)

        self.close()
        self.reference_window.show()

    def open_reference_tables(self):
        import app.reference as reference_tables
        self.reference_pages = reference_tables.ReferencesPage(self.login)
        self.close()
        self.reference_pages.show()

    def fill_data(self):
        if self.selected_reference == 'Warehouse':
            reference_data = db_utils.Warehouse()
        elif self.selected_reference == 'Units':
            reference_data = db_utils.Units()
        elif self.selected_reference == 'Counterparty':
            reference_data = db_utils.Counterparty()
        elif self.selected_reference == 'Goods':
            reference_data = db_utils.Goods()

        items_data = reference_data.select_all_records()
        self.reference_tables.setRowCount(len(items_data))
        tablerow = 0
        for row in items_data:
            self.reference_tables.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.reference_tables.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow += 1

    def delete_data(self):
        selected_row = self.reference_tables.currentRow()
        if selected_row != -1:
            item_id = self.reference_tables.item(selected_row, 0).text()
            item_name = self.reference_tables.item(selected_row, 1).text()

        if self.selected_reference == 'Warehouse':
            delete_record = db_utils.Warehouse()
        elif self.selected_reference == 'Units':
            delete_record = db_utils.Units()
        elif self.selected_reference == 'Counterparty':
            delete_record = db_utils.Counterparty()
        elif self.selected_reference == 'Goods':
            delete_record = db_utils.Goods()

        delete_record.delete_record(item_id)
        self.fill_data()

