import sys
import forms.home_page as home_page
import main

from PyQt5 import QtWidgets
from app.reference import ReferencesPage
from app.documents_tables_form import DocumentPage


class MainWindow(QtWidgets.QMainWindow, home_page.Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.login = login
        self.greetings_label.setText(f'Nice to meet you, {login}')
        self.username.setText(login)
        self.pressing_reference_tables()
        self.pressing_logout()
        self.pressing_procurement()
        self.pressing_sales()

    def pressing_reference_tables(self):
        self.reference.clicked.connect(lambda: self.open_reference_tables())

    def pressing_logout(self):
        self.logout.clicked.connect(lambda: self.open_login_form())

    def pressing_procurement(self):
        self.procurement.clicked.connect(lambda: self.open_document_form('Procurement'))

    def pressing_sales(self):
        self.sales.clicked.connect(lambda: self.open_document_form('Sales'))

    def open_login_form(self):
        import main as login_form
        self.main_window = login_form.App()
        self.close()
        self.main_window.show()

    def open_reference_tables(self):
        self.reference_pages = ReferencesPage(self.login)
        self.close()
        self.reference_pages.show()

    def open_document_form(self, doc_type):
        self.document_pages = DocumentPage(self.login, doc_type)
        self.close()
        self.document_pages.show()