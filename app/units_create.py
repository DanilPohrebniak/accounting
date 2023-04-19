import sys
import utils.db_utils as db_utils
import forms.units_warehouse_create as units_create

from PyQt5 import QtWidgets



class UnitsCreate(QtWidgets.QMainWindow, units_create.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.pressing_reference_tables()
        self.pressing_save()

    def pressing_reference_tables(self):
        self.reference.clicked.connect(lambda: self.open_reference_tables())

    def pressing_save(self):
        self.save.clicked.connect(lambda: self.save_element())

    def open_reference_tables(self):
        import app.reference as reference_tables
        self.reference_pages = reference_tables.ReferencesPage()
        self.close()
        self.reference_pages.show()

    def save_element(self):
        if not self.user.text() == '':
            element = db_utils.Units()
            if element.add_item(self.user.text()):
                import app.reference_tables_form as rtf
                self.main_window = rtf.ReferencesShow('Units')
                self.close()
                self.main_window.show()
            else:
                self.info_message.setText('Item already exists in the units.')
        else:
            self.info_message.setText('The field "Name" is not filled in')