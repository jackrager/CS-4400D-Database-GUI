import sqlite3 as sql
import hashlib
import uuid
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    qApp,
    QAction,
    QWidget,
    QTableView,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QDialog,
    QComboBox,
    QLabel,
    QListView,
    QLineEdit,
    QStackedWidget
)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem
)
from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QVariant,
    QCoreApplication
)

from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlQuery,
    QSqlQueryModel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Atlanta Farms, Gardens, and Orchards GUI")
        left, top, width, height = 0, 700, 500, 500
        self.setGeometry(left, top, width, height)

        #Different Page Widgets
        self.login= QWidget()
        self.newVisitor = QWidget()
        self.newOwner = QWidget()
        self.ownerMain = QWidget()
        self.adminMain = QWidget()
        self.visitMain = QWidget()

        #Main Stacked Widget and Adding the other Pages
        self.stacked_widget = QStackedWidget()
        self.index = self.stacked_widget.currentIndex()
        self.stacked_widget.addWidget(self.login)
        self.stacked_widget.addWidget(self.newVisitor)
        self.stacked_widget.addWidget(self.newOwner)
        self.stacked_widget.addWidget(self.ownerMain)
        self.stacked_widget.addWidget(self.adminMain)
        self.stacked_widget.addWidget(Self.visitMain)

        #Initiate the Login Screen
        self.setCentralWidget(self.stacked_widget)
        self.login_screen()

    def login_screen(self):
        self.stacked_widget.setCurrentIndex(0)
        self.gloginT = QVBoxLayout()
        self.login.setLayout(self.gloginT)
        self.title = QLabel("Atlanta Farms, Gardens, and Orchards")
        self.gloginT.addWidget(self.title)
        self.gloginE = QHBoxLayout()
        self.gloginE.addWidget(QLabel("Email: "))
        self.emailAdd = QLineEdit()
        self.gloginE.addWidget(self.emailAdd)
        self.gloginP = QHBoxLayout()
        self.gloginP.addWidget(QLabel("Password: "))
        self.passAdd = QLineEdit()
        self.gloginP.addWidget(self.passAdd)
        self.gloginN = QHBoxLayout()
        self.newownerB = QPushButton("New Owner Registration")
        self.newvisitorB = QPushButton("New Visitor Registration")
        self.newvisitorB.clicked.connect(self.new_visitor)
        self.newownerB.clicked.connect(self.new_owner)
        self.gloginN.addWidget(self.newvisitorB)
        self.gloginN.addWidget(self.newownerB)
        self.gloginT.addLayout(self.gloginE)
        self.gloginT.addLayout(self.gloginP)
        self.gloginL = QPushButton("Login")
        self.gloginT.addWidget(self.gloginL)
        self.gloginT.addLayout(self.gloginN)

    def new_visitor(self):
        self.stacked_widget.setCurrentIndex(1) 
        self.nvisitT = QVBoxLayout()
        self.newVisitor.setLayout(self.nvisitT)
        self.vrtitle = QLabel("New Visitor Registration")
        self.nvisitT.addWidget(self.vrtitle)
        self.nvisitE = QHBoxLayout()
        self.nvisitE.addWidget(QLabel("Email:*"))
        self.visiteAdd = QLineEdit()
        self.nvisitE.addWidget(self.visiteAdd)
        self.nvisitT.addLayout(self.nvisitE)
        self.nvisitU = QHBoxLayout()
        self.nvisitU.addWidget(QLabel("Username:*"))
        self.visituAdd = QLineEdit()
        self.nvisitU.addWidget(self.visituAdd)
        self.nvisitT.addLayout(self.nvisitU)
        self.nvisitP = QHBoxLayout()
        self.nvisitP.addWidget(QLabel("Password:*"))
        self.visitpAdd = QLineEdit()
        self.nvisitP.addWidget(self.visitpAdd)
        self.nvisitT.addLayout(self.nvisitP)
        self.nvisitC = QHBoxLayout()
        self.nvisitC.addWidget(QLabel("Confirm Password:*"))
        self.visitcAdd = QLineEdit()
        self.nvisitC.addWidget(self.visitcAdd)
        self.nvisitT.addLayout(self.nvisitC)
        self.nvisitR = QHBoxLayout()
        self.nvisitRB = QPushButton("Register Visitor")
        self.nvisitCB = QPushButton("Cancel")
        self.nvisitCB.clicked.connect(self.cancel)
        self.nvisitR.addWidget(self.nvisitRB)
        self.nvisitR.addWidget(self.nvisitCB)
        self.nvisitT.addLayout(self.nvisitR)

    def new_owner(self):
        self.stacked_widget.setCurrentIndex(2) 
        self.nownerT = QVBoxLayout()
        self.newOwner.setLayout(self.nownerT)
        self.ortitle = QLabel("New Owner Registration")
        self.nownerT.addWidget(self.ortitle)
        self.nownerE = QHBoxLayout()
        self.nownerE.addWidget(QLabel("Email:*"))
        self.ownereAdd = QLineEdit()
        self.nownerE.addWidget(self.ownereAdd)
        self.nownerT.addLayout(self.nownerE)
        self.nownerU = QHBoxLayout()
        self.nownerU.addWidget(QLabel("Username:*"))
        self.owneruAdd = QLineEdit()
        self.nownerU.addWidget(self.owneruAdd)
        self.nownerT.addLayout(self.nownerU)
        self.nownerP = QHBoxLayout()
        self.nownerP.addWidget(QLabel("Password:*"))
        self.ownerpAdd = QLineEdit()
        self.nownerP.addWidget(self.ownerpAdd)
        self.nownerT.addLayout(self.nownerP)
        self.nownerC = QHBoxLayout()
        self.nownerC.addWidget(QLabel("Confirm Password:*"))
        self.ownercAdd = QLineEdit()
        self.nownerC.addWidget(self.ownercAdd)
        self.nownerT.addLayout(self.nownerC)
        self.nownerPR = QHBoxLayout()
        self.nownerPR.addWidget(QLabel("Property Name:*"))
        self.ownerprAdd = QLineEdit()
        self.nownerPR.addWidget(self.ownerprAdd)
        self.nownerT.addLayout(self.nownerPR)
        self.nownerA = QHBoxLayout()
        self.nownerA.addWidget(QLabel("Street Address:*"))
        self.owneraAdd = QLineEdit()
        self.nownerA.addWidget(self.owneraAdd)
        self.nownerT.addLayout(self.nownerA)
        self.nownerCZA = QHBoxLayout()
        self.nownerCZA.addWidget(QLabel("City:*"))
        self.nownerCI = QLineEdit()
        self.nownerCZA.addWidget(self.nownerCI)
        self.nownerCZA.addWidget(QLabel("Zip:*"))
        self.nownerZ = QLineEdit()
        self.nownerCZA.addWidget(self.nownerZ)
        self.nownerCZA.addWidget(QLabel("Acres:*"))
        self.nownerAC = QLineEdit()
        self.nownerCZA.addWidget(self.nownerAC)
        self.nownerT.addLayout(self.nownerCZA)
        self.nownerTPC = QHBoxLayout()
        self.nownerTPC.addWidget(QLabel("Property Type:*"))
        self.nownerTY = QComboBox()
        self.nownerTPC.addWidget(self.nownerTY)
        self.nownerTPC.addWidget(QLabel("Public:*"))
        self.nownerPU = QComboBox()
        self.nownerTPC.addWidget(self.nownerPU)
        self.nownerTPC.addWidget(QLabel("Commercial:*"))
        self.nownerCO = QComboBox()
        self.nownerTPC.addWidget(self.nownerCO)
        self.nownerT.addLayout(self.nownerTPC)
        self.nownerANCR = QHBoxLayout()
        self.nownerANCR.addWidget(QLabel("Animal:*"))
        self.nownerAN = QComboBox()
        self.nownerANCR.addWidget(self.nownerAN)
        self.nownerANCR.addWidget(QLabel("Crop:*"))
        self.nownerCR = QComboBox()
        self.nownerANCR.addWidget(self.nownerCR)
        self.nownerT.addLayout(self.nownerANCR)
        self.nownerR = QHBoxLayout()
        self.nownerRB = QPushButton("Register Owner")
        self.nownerCB = QPushButton("Cancel")
        self.nownerCB.clicked.connect(self.cancel)
        self.nownerR.addWidget(self.nownerRB)
        self.nownerR.addWidget(self.nownerCB)
        self.nownerT.addLayout(self.nownerR)


    def cancel(self):
        self.stacked_widget.setCurrentIndex(0)

    def hash_password(self):
        pass

    def owner_main(self):
        self.stacked_widget.setCurrentIndex(3)
        self.ownerMainT = QVBoxLayout()

    def admin_main(self):
        self.stacked_widget.setCurrentIndex(4) 
        self.adminMainT = QVBoxLayout()
        self.adminMainT.addWidget((QLabel("Welcome")))
        self.aViewVisit = QPushButton("View Visitors List")
        self.adminMainT.addWidget(self.aViewVisit)
        #connect
        self.aViewOwner = QPushButton("View Owners List")
        self.adminMainT.addWidget(self.aViewOwner)
        #connect
        self.aViewConfirmed = QPushButton("View Confirmed Properties")
        self.adminMainT.addWidget(self.aViewConfirmed)
        #connect
        self.aViewUnconfirmed = QPushButton("View Unconfirmed Properties")
        self.adminMainT.addWidget(self.aViewUnconfirmed)
        #connect
        self.aViewApproved = QPushButton("View Approved Animals and Crops")
        self.adminMainT.addWidget(self.aViewApproved)
        #connect
        self.aViewPending = QPushButton("View Pending Animals and Crops")
        self.adminMainT.addWidget(self.aViewVisit)
        #connect

    def visitor_main(self):
        self.stacked_widget.setCurrentIndex(5)
        self.visitMainT = QVBoxLayout()

    def add_property(self):
        #mostly the same as new owner
        pass

    def new_thing(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())