import sys
import utils.db_utils as db_utils
import forms.units_warehouse_create as units_create

from PyQt5 import QtWidgets



class UnitsCreate(QtWidgets.QMainWindow, units_create.Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.login = login
        self.username.setText(login)
        self.pressing_reference_tables()
        self.pressing_save()
        self.pressing_logout()

    def pressing_reference_tables(self):
        self.reference.clicked.connect(lambda: self.open_reference_tables())

    def pressing_save(self):
        self.save.clicked.connect(lambda: self.save_element())

    def pressing_logout(self):
        self.logout.clicked.connect(lambda: self.open_login_form())

    def open_login_form(self):
        import main as login_form
        self.main_window = login_form.App()
        self.close()
        self.main_window.show()

    def open_reference_tables(self):
        import app.reference as reference_tables
        self.reference_pages = reference_tables.ReferencesPage(self.login)
        self.close()
        self.reference_pages.show()

    def save_element(self):
        if not self.user.text() == '':
            element = db_utils.Units()
            if element.add_item(self.user.text()):
                import app.reference_tables_form as rtf
                self.main_window = rtf.ReferencesShow('Units', self.login)
                self.close()
                self.main_window.show()
            else:
                self.info_message.setText('Item already exists in the units.')
        else:
            self.info_message.setText('The field "Name" is not filled in')