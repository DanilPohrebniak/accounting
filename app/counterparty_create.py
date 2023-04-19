import sys
import utils.db_utils as db_utils
import forms.counterparty_create as counterparty_create

from PyQt5 import QtWidgets



class CounterpartyCreate(QtWidgets.QMainWindow, counterparty_create.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1900, 1080)
        self.setWindowTitle('Accounting')
        self.pressing_reference_tables()
        self.pressing_save()
        self.first_name.textChanged.connect(self.on_text_changed)
        self.last_name.textChanged.connect(self.on_text_changed)

    def pressing_reference_tables(self):
        self.reference.clicked.connect(lambda: self.open_reference_tables())

    def pressing_save(self):
        self.save.clicked.connect(lambda: self.save_element())

    def on_text_changed(self):
        self.name.setText(self.first_name.text() + ' ' + self.last_name.text())

    def open_reference_tables(self):
        import app.reference as reference_tables
        self.reference_pages = reference_tables.ReferencesPage()
        self.close()
        self.reference_pages.show()

    def save_element(self):
        if not self.name.text() == '':
            element = db_utils.Counterparty()
            if element.add_item(self.name.text(),
                                self.first_name.text(),
                                self.last_name.text(),
                                self.id_card.text(),
                                self.phone.text()):
                import app.reference_tables_form as rtf
                self.main_window = rtf.ReferencesShow('Counterparty')
                self.close()
                self.main_window.show()
            else:
                self.info_message.setText('Item already exists in the counterparty.')
        else:
            self.info_message.setText('The field "Name" is not filled in')