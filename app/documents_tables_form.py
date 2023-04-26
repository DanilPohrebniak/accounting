import sys
import forms.documents_form as documents_page

from PyQt5 import QtWidgets
from app.reference_tables_form import ReferencesShow
from app.reference import ReferencesPage
from app.document_create import DocumentCreate



class DocumentPage(QtWidgets.QMainWindow, documents_page.Ui_MainWindow):
    def __init__(self, login, doc_type):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.login = login
        self.username.setText(login)
        self.doc_type = doc_type
        self.pressing_logout()
        self.pressing_reference_tables()
        self.pressing_sales()
        self.pressing_procurement()
        self.pressing_add()

    def pressing_logout(self):
        self.logout.clicked.connect(lambda: self.open_login_form())

    def pressing_reference_tables(self):
        self.reference.clicked.connect(lambda: self.open_reference_tables())

    def pressing_procurement(self):
        if not self.doc_type == 'Procurement':
            self.procurement.clicked.connect(lambda: self.open_document_form('Procurement'))

    def pressing_sales(self):
        if not self.doc_type == 'Sales':
            self.sales.clicked.connect(lambda: self.open_document_form('Sales'))

    def pressing_add(self):
        self.add.clicked.connect(lambda: self.create_document())

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

    def create_document(self):
        self.document_create = DocumentCreate(self.login, self.doc_type)
        self.close()
        self.document_create.show()
