# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\PyQt\accounting\design\main_surface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 1098)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QGroupBox { border: none; }\n"
"QPushButton {\n"
"    border: none;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    color: grey;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox.setSizePolicy(sizePolicy)
        self.horizontalGroupBox.setMaximumSize(QtCore.QSize(1920, 1080))
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.horizontalGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Left_side = QtWidgets.QGroupBox(self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Left_side.sizePolicy().hasHeightForWidth())
        self.Left_side.setSizePolicy(sizePolicy)
        self.Left_side.setMaximumSize(QtCore.QSize(300, 1080))
        self.Left_side.setStyleSheet("background: #EBEBEB;\n"
"border-radius: 10px;\n"
"")
        self.Left_side.setObjectName("Left_side")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Left_side)
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.Left_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalGroupBox.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox.setSizePolicy(sizePolicy)
        self.verticalGroupBox.setStyleSheet("")
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.procurement_nav = QtWidgets.QFrame(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.procurement_nav.sizePolicy().hasHeightForWidth())
        self.procurement_nav.setSizePolicy(sizePolicy)
        self.procurement_nav.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.procurement_nav.setFont(font)
        self.procurement_nav.setObjectName("procurement_nav")
        self.income_nav = QtWidgets.QHBoxLayout(self.procurement_nav)
        self.income_nav.setObjectName("income_nav")
        self.procurement_pic = QtWidgets.QLabel(self.procurement_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.procurement_pic.sizePolicy().hasHeightForWidth())
        self.procurement_pic.setSizePolicy(sizePolicy)
        self.procurement_pic.setMaximumSize(QtCore.QSize(32, 32))
        self.procurement_pic.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.procurement_pic.setFont(font)
        self.procurement_pic.setText("")
        self.procurement_pic.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/procurement.png"))
        self.procurement_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.procurement_pic.setObjectName("procurement_pic")
        self.income_nav.addWidget(self.procurement_pic)
        self.procurement = QtWidgets.QPushButton(self.procurement_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.procurement.sizePolicy().hasHeightForWidth())
        self.procurement.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.procurement.setFont(font)
        self.procurement.setStyleSheet("")
        self.procurement.setObjectName("procurement")
        self.income_nav.addWidget(self.procurement)
        self.verticalLayout_2.addWidget(self.procurement_nav)
        self.sales_nav_2 = QtWidgets.QFrame(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sales_nav_2.sizePolicy().hasHeightForWidth())
        self.sales_nav_2.setSizePolicy(sizePolicy)
        self.sales_nav_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.sales_nav_2.setFont(font)
        self.sales_nav_2.setObjectName("sales_nav_2")
        self.expense_nav = QtWidgets.QHBoxLayout(self.sales_nav_2)
        self.expense_nav.setObjectName("expense_nav")
        self.sales_pic = QtWidgets.QLabel(self.sales_nav_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sales_pic.sizePolicy().hasHeightForWidth())
        self.sales_pic.setSizePolicy(sizePolicy)
        self.sales_pic.setMinimumSize(QtCore.QSize(0, 0))
        self.sales_pic.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.sales_pic.setFont(font)
        self.sales_pic.setText("")
        self.sales_pic.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/cash-register.png"))
        self.sales_pic.setObjectName("sales_pic")
        self.expense_nav.addWidget(self.sales_pic)
        self.sales = QtWidgets.QPushButton(self.sales_nav_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sales.sizePolicy().hasHeightForWidth())
        self.sales.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.sales.setFont(font)
        self.sales.setStyleSheet("")
        self.sales.setObjectName("sales")
        self.expense_nav.addWidget(self.sales)
        self.verticalLayout_2.addWidget(self.sales_nav_2)
        self.inventory_nav = QtWidgets.QFrame(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventory_nav.sizePolicy().hasHeightForWidth())
        self.inventory_nav.setSizePolicy(sizePolicy)
        self.inventory_nav.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.inventory_nav.setFont(font)
        self.inventory_nav.setObjectName("inventory_nav")
        self.goods_nav = QtWidgets.QHBoxLayout(self.inventory_nav)
        self.goods_nav.setObjectName("goods_nav")
        self.inventory_pic = QtWidgets.QLabel(self.inventory_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventory_pic.sizePolicy().hasHeightForWidth())
        self.inventory_pic.setSizePolicy(sizePolicy)
        self.inventory_pic.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.inventory_pic.setFont(font)
        self.inventory_pic.setText("")
        self.inventory_pic.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/inventory.png"))
        self.inventory_pic.setObjectName("inventory_pic")
        self.goods_nav.addWidget(self.inventory_pic)
        self.inventory = QtWidgets.QPushButton(self.inventory_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventory.sizePolicy().hasHeightForWidth())
        self.inventory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.inventory.setFont(font)
        self.inventory.setStyleSheet("")
        self.inventory.setObjectName("inventory")
        self.goods_nav.addWidget(self.inventory)
        self.verticalLayout_2.addWidget(self.inventory_nav)
        self.reference_nav = QtWidgets.QFrame(self.verticalGroupBox)
        self.reference_nav.setMinimumSize(QtCore.QSize(0, 50))
        self.reference_nav.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reference_nav.setObjectName("reference_nav")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.reference_nav)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.reference_nav)
        self.label_3.setMaximumSize(QtCore.QSize(32, 32))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/research.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.reference = QtWidgets.QPushButton(self.reference_nav)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.reference.setFont(font)
        self.reference.setObjectName("reference")
        self.horizontalLayout.addWidget(self.reference)
        self.verticalLayout_2.addWidget(self.reference_nav)
        self.gridLayout_5.addWidget(self.verticalGroupBox, 3, 0, 1, 1)
        self.verticalGroupBox1 = QtWidgets.QGroupBox(self.Left_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalGroupBox1.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox1.setSizePolicy(sizePolicy)
        self.verticalGroupBox1.setMinimumSize(QtCore.QSize(0, 630))
        self.verticalGroupBox1.setStyleSheet("")
        self.verticalGroupBox1.setObjectName("verticalGroupBox1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_5.addWidget(self.verticalGroupBox1, 4, 0, 1, 1)
        self.menu_list = QtWidgets.QLabel(self.Left_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_list.sizePolicy().hasHeightForWidth())
        self.menu_list.setSizePolicy(sizePolicy)
        self.menu_list.setMinimumSize(QtCore.QSize(300, 50))
        self.menu_list.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.menu_list.setFont(font)
        self.menu_list.setAlignment(QtCore.Qt.AlignCenter)
        self.menu_list.setObjectName("menu_list")
        self.gridLayout_5.addWidget(self.menu_list, 1, 0, 1, 1)
        self.app_name = QtWidgets.QLabel(self.Left_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_name.sizePolicy().hasHeightForWidth())
        self.app_name.setSizePolicy(sizePolicy)
        self.app_name.setMinimumSize(QtCore.QSize(300, 200))
        self.app_name.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.app_name.setFont(font)
        self.app_name.setWhatsThis("")
        self.app_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.app_name.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.app_name.setAlignment(QtCore.Qt.AlignCenter)
        self.app_name.setObjectName("app_name")
        self.gridLayout_5.addWidget(self.app_name, 0, 0, 1, 1)
        self.separator = QtWidgets.QFrame(self.Left_side)
        self.separator.setMinimumSize(QtCore.QSize(0, 2))
        self.separator.setMaximumSize(QtCore.QSize(16777215, 2))
        self.separator.setStyleSheet("background-color: rgb(145, 145, 145);")
        self.separator.setFrameShape(QtWidgets.QFrame.Panel)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator.setObjectName("separator")
        self.gridLayout_5.addWidget(self.separator, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.Left_side, 0, 0, 1, 1)
        self.Right_side = QtWidgets.QGroupBox(self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(162)
        sizePolicy.setVerticalStretch(108)
        sizePolicy.setHeightForWidth(self.Right_side.sizePolicy().hasHeightForWidth())
        self.Right_side.setSizePolicy(sizePolicy)
        self.Right_side.setMaximumSize(QtCore.QSize(1620, 1080))
        self.Right_side.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Right_side.setStyleSheet("")
        self.Right_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Right_side.setObjectName("Right_side")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Right_side)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Header_block = QtWidgets.QGroupBox(self.Right_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header_block.sizePolicy().hasHeightForWidth())
        self.Header_block.setSizePolicy(sizePolicy)
        self.Header_block.setMinimumSize(QtCore.QSize(800, 100))
        self.Header_block.setMaximumSize(QtCore.QSize(1620, 100))
        self.Header_block.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Header_block.setObjectName("Header_block")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Header_block)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.User_info = QtWidgets.QGroupBox(self.Header_block)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.User_info.sizePolicy().hasHeightForWidth())
        self.User_info.setSizePolicy(sizePolicy)
        self.User_info.setMaximumSize(QtCore.QSize(1620, 100))
        self.User_info.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.User_info.setObjectName("User_info")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.User_info)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.notifications = QtWidgets.QPushButton(self.User_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notifications.sizePolicy().hasHeightForWidth())
        self.notifications.setSizePolicy(sizePolicy)
        self.notifications.setMaximumSize(QtCore.QSize(16777215, 50))
        self.notifications.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.notifications.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/bell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notifications.setIcon(icon)
        self.notifications.setIconSize(QtCore.QSize(40, 40))
        self.notifications.setObjectName("notifications")
        self.gridLayout_3.addWidget(self.notifications, 0, 0, 1, 1)
        self.username = QtWidgets.QLabel(self.User_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMaximumSize(QtCore.QSize(90, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username.setObjectName("username")
        self.gridLayout_3.addWidget(self.username, 0, 1, 1, 1)
        self.logout = QtWidgets.QPushButton(self.User_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout.sizePolicy().hasHeightForWidth())
        self.logout.setSizePolicy(sizePolicy)
        self.logout.setMaximumSize(QtCore.QSize(45, 40))
        self.logout.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.logout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon1)
        self.logout.setIconSize(QtCore.QSize(40, 40))
        self.logout.setObjectName("logout")
        self.gridLayout_3.addWidget(self.logout, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.User_info, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.Header_block, 0, 0, 1, 1)
        self.Body_block = QtWidgets.QGroupBox(self.Right_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Body_block.sizePolicy().hasHeightForWidth())
        self.Body_block.setSizePolicy(sizePolicy)
        self.Body_block.setMaximumSize(QtCore.QSize(1620, 980))
        self.Body_block.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.Body_block.setObjectName("Body_block")
        self.gridLayout = QtWidgets.QGridLayout(self.Body_block)
        self.gridLayout.setObjectName("gridLayout")
        self.task_block = QtWidgets.QGroupBox(self.Body_block)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_block.sizePolicy().hasHeightForWidth())
        self.task_block.setSizePolicy(sizePolicy)
        self.task_block.setMinimumSize(QtCore.QSize(0, 0))
        self.task_block.setMaximumSize(QtCore.QSize(250, 1080))
        self.task_block.setStyleSheet("background: #EBEBEB;\n"
"border-radius: 10px;\n"
"")
        self.task_block.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.task_block.setFlat(False)
        self.task_block.setObjectName("task_block")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.task_block)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tasks_label = QtWidgets.QLabel(self.task_block)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tasks_label.sizePolicy().hasHeightForWidth())
        self.tasks_label.setSizePolicy(sizePolicy)
        self.tasks_label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.tasks_label.setFont(font)
        self.tasks_label.setWhatsThis("")
        self.tasks_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tasks_label.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.tasks_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tasks_label.setObjectName("tasks_label")
        self.gridLayout_8.addWidget(self.tasks_label, 0, 0, 1, 1)
        self.task_2 = QtWidgets.QLabel(self.task_block)
        self.task_2.setText("")
        self.task_2.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/task_2.png"))
        self.task_2.setAlignment(QtCore.Qt.AlignCenter)
        self.task_2.setObjectName("task_2")
        self.gridLayout_8.addWidget(self.task_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.task_block)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/task_3.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 2, 0, 1, 1)
        self.task_1 = QtWidgets.QLabel(self.task_block)
        self.task_1.setStyleSheet("")
        self.task_1.setText("")
        self.task_1.setPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/task_1.png"))
        self.task_1.setAlignment(QtCore.Qt.AlignCenter)
        self.task_1.setObjectName("task_1")
        self.gridLayout_8.addWidget(self.task_1, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.task_block, 0, 5, 1, 1)
        self.items_in_body = QtWidgets.QGroupBox(self.Body_block)
        self.items_in_body.setMinimumSize(QtCore.QSize(200, 100))
        self.items_in_body.setMaximumSize(QtCore.QSize(1370, 980))
        self.items_in_body.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.items_in_body.setObjectName("items_in_body")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.items_in_body)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalGroupBox1 = QtWidgets.QGroupBox(self.items_in_body)
        self.horizontalGroupBox1.setMinimumSize(QtCore.QSize(50, 0))
        self.horizontalGroupBox1.setMaximumSize(QtCore.QSize(500, 100))
        self.horizontalGroupBox1.setObjectName("horizontalGroupBox1")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.horizontalGroupBox1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton = QtWidgets.QPushButton(self.horizontalGroupBox1)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\Python\\PyQt\\accounting\\design\\icons/waving-hand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_10.addWidget(self.pushButton, 0, 0, 1, 1)
        self.greetings_label = QtWidgets.QLabel(self.horizontalGroupBox1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greetings_label.sizePolicy().hasHeightForWidth())
        self.greetings_label.setSizePolicy(sizePolicy)
        self.greetings_label.setMaximumSize(QtCore.QSize(1300, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.greetings_label.setFont(font)
        self.greetings_label.setText("")
        self.greetings_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.greetings_label.setObjectName("greetings_label")
        self.gridLayout_10.addWidget(self.greetings_label, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.horizontalGroupBox1, 0, 0, 1, 1)
        self.verticalGroupBox2 = QtWidgets.QGroupBox(self.items_in_body)
        self.verticalGroupBox2.setMinimumSize(QtCore.QSize(0, 800))
        self.verticalGroupBox2.setObjectName("verticalGroupBox2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.verticalGroupBox2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 750))
        self.label_2.setLineWidth(2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.verticalGroupBox2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.items_in_body, 0, 4, 1, 1)
        self.gridLayout_4.addWidget(self.Body_block, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.Right_side, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.horizontalGroupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.procurement.setText(_translate("MainWindow", "Procurement"))
        self.sales.setText(_translate("MainWindow", "Sales"))
        self.inventory.setText(_translate("MainWindow", "Inventory"))
        self.reference.setText(_translate("MainWindow", "Reference tables"))
        self.menu_list.setText(_translate("MainWindow", "     Menu"))
        self.app_name.setText(_translate("MainWindow", "Accounting"))
        self.username.setText(_translate("MainWindow", "Admin"))
        self.tasks_label.setText(_translate("MainWindow", "Tasks"))
