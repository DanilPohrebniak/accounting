import sys
import forms.login as login

from PyQt5 import QtWidgets
# from app.main_menu import MainWindow


class App(QtWidgets.QMainWindow, login.Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pressing_login()

    def pressing_login(self):
        self.loginButton.clicked.connect(lambda: self.filling_check())

    def filling_check(self):
        if self.username.text() == '' or self.password.text() == '':
            self.info_message.setText('Check the fields')
            return
        self.info_message.setText('')
        self.cheking()

    def cheking(self):
        import app.main_menu as mw
        if self.user.check_user(self.username.text(), self.password.text()):
            self.main_window = mw.MainWindow(self.username.text())
            self.close()
            self.main_window.show()
        else:
            self.info_message.setText('Check the entered data')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()