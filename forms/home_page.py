from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 746)
        MainWindow.setStyleSheet("QGroupBox { border: none; }\n"
"QPushButton {\n"
"    border: none;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    color: grey;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setGeometry(QtCore.QRect(0, 10, 250, 1080))
        self.verticalGroupBox.setStyleSheet("background: #EBEBEB;\n"
"")
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 3)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.app_name = QtWidgets.QLabel(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_name.sizePolicy().hasHeightForWidth())
        self.app_name.setSizePolicy(sizePolicy)
        self.app_name.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.app_name.setFont(font)
        self.app_name.setWhatsThis("")
        self.app_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.app_name.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.app_name.setAlignment(QtCore.Qt.AlignCenter)
        self.app_name.setObjectName("app_name")
        self.verticalLayout.addWidget(self.app_name)
        self.menu_list = QtWidgets.QLabel(self.verticalGroupBox)
        self.menu_list.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.menu_list.setFont(font)
        self.menu_list.setAlignment(QtCore.Qt.AlignCenter)
        self.menu_list.setObjectName("menu_list")
        self.verticalLayout.addWidget(self.menu_list)
        self.verticalGroupBox1 = QtWidgets.QGroupBox(self.verticalGroupBox)
        self.verticalGroupBox1.setStyleSheet("")
        self.verticalGroupBox1.setObjectName("verticalGroupBox1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.procurement_nav = QtWidgets.QFrame(self.verticalGroupBox1)
        self.procurement_nav.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.procurement_nav.setFont(font)
        self.procurement_nav.setObjectName("procurement_nav")
        self.income_nav = QtWidgets.QHBoxLayout(self.procurement_nav)
        self.income_nav.setObjectName("income_nav")
        self.procurement_pic = QtWidgets.QLabel(self.procurement_nav)
        self.procurement_pic.setMaximumSize(QtCore.QSize(24, 24))
        self.procurement_pic.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.procurement_pic.setFont(font)
        self.procurement_pic.setText("")
        self.procurement_pic.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/local_mall_black_24dp.svg"))
        self.procurement_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.procurement_pic.setObjectName("procurement_pic")
        self.income_nav.addWidget(self.procurement_pic)
        self.procurement = QtWidgets.QPushButton(self.procurement_nav)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.procurement.setFont(font)
        self.procurement.setStyleSheet("")
        self.procurement.setObjectName("procurement")
        self.income_nav.addWidget(self.procurement)
        self.verticalLayout_2.addWidget(self.procurement_nav)
        self.sales_nav_2 = QtWidgets.QFrame(self.verticalGroupBox1)
        self.sales_nav_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.sales_nav_2.setFont(font)
        self.sales_nav_2.setObjectName("sales_nav_2")
        self.expense_nav = QtWidgets.QHBoxLayout(self.sales_nav_2)
        self.expense_nav.setObjectName("expense_nav")
        self.sales_pic = QtWidgets.QLabel(self.sales_nav_2)
        self.sales_pic.setMinimumSize(QtCore.QSize(0, 0))
        self.sales_pic.setMaximumSize(QtCore.QSize(24, 24))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.sales_pic.setFont(font)
        self.sales_pic.setText("")
        self.sales_pic.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/local_grocery_store_black_24dp.svg"))
        self.sales_pic.setObjectName("sales_pic")
        self.expense_nav.addWidget(self.sales_pic)
        self.sales = QtWidgets.QPushButton(self.sales_nav_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.sales.setFont(font)
        self.sales.setStyleSheet("")
        self.sales.setObjectName("sales")
        self.expense_nav.addWidget(self.sales)
        self.verticalLayout_2.addWidget(self.sales_nav_2)
        self.inventory_nav = QtWidgets.QFrame(self.verticalGroupBox1)
        self.inventory_nav.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.inventory_nav.setFont(font)
        self.inventory_nav.setObjectName("inventory_nav")
        self.goods_nav = QtWidgets.QHBoxLayout(self.inventory_nav)
        self.goods_nav.setObjectName("goods_nav")
        self.inventory_pic = QtWidgets.QLabel(self.inventory_nav)
        self.inventory_pic.setMaximumSize(QtCore.QSize(24, 24))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.inventory_pic.setFont(font)
        self.inventory_pic.setText("")
        self.inventory_pic.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/local_cafe_black_24dp.svg"))
        self.inventory_pic.setObjectName("inventory_pic")
        self.goods_nav.addWidget(self.inventory_pic)
        self.inventory = QtWidgets.QPushButton(self.inventory_nav)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.inventory.setFont(font)
        self.inventory.setStyleSheet("")
        self.inventory.setObjectName("inventory")
        self.goods_nav.addWidget(self.inventory)
        self.verticalLayout_2.addWidget(self.inventory_nav)
        self.verticalLayout.addWidget(self.verticalGroupBox1)
        self.verticalGroupBox2 = QtWidgets.QGroupBox(self.verticalGroupBox)
        self.verticalGroupBox2.setMinimumSize(QtCore.QSize(0, 630))
        self.verticalGroupBox2.setStyleSheet("")
        self.verticalGroupBox2.setObjectName("verticalGroupBox2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addWidget(self.verticalGroupBox2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 130, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_name.setText(_translate("MainWindow", "Accounting"))
        self.menu_list.setText(_translate("MainWindow", "Menu"))
        self.procurement.setText(_translate("MainWindow", "Procurement"))
        self.sales.setText(_translate("MainWindow", "Sales"))
        self.inventory.setText(_translate("MainWindow", "Inventory"))
        self.label.setText(_translate("MainWindow", "Nice to meet you, [UserName]"))
