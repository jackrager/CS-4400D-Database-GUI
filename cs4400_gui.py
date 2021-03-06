import pymysql as sql
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

        self.connection =  sql.connect(host="academic-mysql.cc.gatech.edu",user="cs4400_team_18", password="KD8uc5p2", 
            db="cs4400_team_18",charset="utf8mb4",cursorclass=sql.cursors.DictCursor)
        self.c = self.connection.cursor()

        #Different Page Widgets
        self.login= QWidget()
        self.newVisitor = QWidget()
        self.newOwner = QWidget()

        self.ownerMain = QWidget()
        self.otherOProp = QWidget()
        self.otherOPropDetail = QWidget()
        self.oPropManage = QWidget()
        self.oPropAdd = QWidget()

        self.adminMain = QWidget()
        self.aUnconfirmed = QWidget()
        self.aManage = QWidget()
        self.aConfirmed = QWidget()
        self.aOwner = QWidget()
        self.aVisitor = QWidget()
        self.aApproved = QWidget()
        self.aPending = QWidget()

        self.visitMain = QWidget()
        self.vPropDetail = QWidget()
        self.vVisitHist = QWidget()

        #Main Stacked Widget and Adding the other Pages
        self.stacked_widget = QStackedWidget()
        self.index = self.stacked_widget.currentIndex()
        self.stacked_widget.addWidget(self.login)
        self.stacked_widget.addWidget(self.newVisitor)
        self.stacked_widget.addWidget(self.newOwner)
        self.stacked_widget.addWidget(self.ownerMain)
        self.stacked_widget.addWidget(self.otherOProp)
        self.stacked_widget.addWidget(self.otherOPropDetail)
        self.stacked_widget.addWidget(self.oPropManage)
        self.stacked_widget.addWidget(self.oPropAdd)
        self.stacked_widget.addWidget(self.adminMain)
        self.stacked_widget.addWidget(self.aUnconfirmed)
        self.stacked_widget.addWidget(self.aManage)
        self.stacked_widget.addWidget(self.aConfirmed)
        self.stacked_widget.addWidget(self.aOwner)
        self.stacked_widget.addWidget(self.aVisitor)
        self.stacked_widget.addWidget(self.aApproved)
        self.stacked_widget.addWidget(self.aPending)
        self.stacked_widget.addWidget(self.visitMain)
        self.stacked_widget.addWidget(self.vPropDetail)
        self.stacked_widget.addWidget(self.vVisitHist)

        #Initiate the Login Screen
        self.setCentralWidget(self.stacked_widget)
        self.login_screen()
        
    def cancel(self):
        self.stacked_widget.setCurrentIndex(0)

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
        self.gloginL.clicked.connect(self.login_execute)
        self.gloginT.addWidget(self.gloginL)
        self.gloginT.addLayout(self.gloginN)
        #

    def login_execute(self):
        self.c.execute("select Email, Password from User")
        up = self.c.fetchall()
        for each in up:
            if (self.emailAdd.text() == each['Email'] and self.passAdd.text() == each['Password']):
                self.stacked_widget.setCurrentIndex(3)

        self.c.close()

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
        self.ownerprName = QLineEdit()
        self.nownerPR.addWidget(self.ownerprName)
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

        #c.execute('insert into user values (?,?,?,?)', (self.owneruAdd.text(), self.ownereAdd.text(), self.ownerpAdd.text(), self.TYPE.text()))

        #c.execute('insert into project values (?,?,?,?,?,?,?,?)', (self..text(), self.sicadd.text(), self.nameadd.text(), self.addr1add.text(),
                #self.addr2add.text(), self.cityadd.text(), self.stateadd.text(), int(self.zipadd.text())))

        #c.execute("select company.name from company join sector using(sic) where sector.name = (?)", (sname,))

    def owner_main(self):
        self.stacked_widget.setCurrentIndex(3)
        self.ownerMainT = QVBoxLayout()
        self.ownerMainT.addWidget(QLabel("Welcome"))
        self.ownerBOT = QHoxLayout()
        self.ownerMainT.addLayout(self.ownerBOT)

        self.ownerMainT.addWidget(QLabel("Your Properties"))
        
        self.ownerSEAR = QVBoxLayout()
        self.ownerSearch = QComboBox()
        self.ownerSearchInp = QLineEdit()
        self.ownerSEAR.addWidget(self.ownerSearch)
        self.ownerSEAR.addWidget(self.ownerSearchInp)
        self.ownerBOT.addLayout(self.ownerSEAR)

        self.ownerBUT = QVBoxLayout()
        self.ownerManageBut = QPushButton("Manage Property")
        self.ownerAddBut = QPushButton("Add Property")
        self.ownerViewBut = QPushButton("View Other Properties")
        self.ownerBOT.addLayout(self.ownerBUT)

        self.ownerLogOut = QPushButton()
        self.ownerBOT.addWidget(self.ownerLogOut)
        self.ownerLogOut.clicked.connect(self.cancel())

    def other_o_prop(self):
        self.stacked_widget.setCurrentIndex(4)

    def other_o_prop_detail(self):
        self.stacked_widget.setCurrentIndex(5)

    def o_prop_manage(self):
        self.stacked_widget.setCurrentIndex(6)

    def o_prop_add(self):
        self.stacked_widget.setCurrentIndex(7)

        self.apropT = QVBoxLayout()
        self.addProp.setLayout(self.apropT)

        self.apropPR = QHBoxLayout()
        self.apropPR.addWidget(QLabel("Property Name:*"))
        self.propName = QLineEdit()
        self.apropPR.addWidget(self.propName)
        self.apropT.addLayout(self.apropPR)

        self.apropA = QHBoxLayout()
        self.apropA.addWidget(QLabel("Street Address:*"))
        self.propaAdd = QLineEdit()
        self.npropA.addWidget(self.propaAdd)
        self.npropT.addLayout(self.npropA)

        self.npropCZA = QHBoxLayout()
        self.npropCZA.addWidget(QLabel("City:*"))
        self.npropCI = QLineEdit()
        self.npropCZA.addWidget(self.npropCI)
        self.npropCZA.addWidget(QLabel("Zip:*"))
        self.npropZ = QLineEdit()
        self.npropCZA.addWidget(self.npropZ)
        self.npropCZA.addWidget(QLabel("Acres:*"))
        self.npropAC = QLineEdit()
        self.npropCZA.addWidget(self.npropAC)
        self.npropT.addLayout(self.npropCZA)

        self.npropTPC = QHBoxLayout()
        self.npropTPC.addWidget(QLabel("Property Type:*"))
        self.npropTY = QComboBox()
        self.npropTPC.addWidget(self.npropTY)
        self.npropTPC.addWidget(QLabel("Public:*"))
        self.npropPU = QComboBox()
        self.npropTPC.addWidget(self.npropPU)
        self.npropTPC.addWidget(QLabel("Commercial:*"))
        self.npropCO = QComboBox()
        self.npropTPC.addWidget(self.npropCO)
        self.npropT.addLayout(self.npropTPC)

        self.npropANCR = QHBoxLayout()
        self.npropANCR.addWidget(QLabel("Animal:*"))
        self.npropAN = QComboBox()
        self.npropANCR.addWidget(self.npropAN)
        self.npropANCR.addWidget(QLabel("Crop:*"))
        self.npropCR = QComboBox()
        self.npropANCR.addWidget(self.npropCR)
        self.npropT.addLayout(self.npropANCR)

        self.npropR = QHBoxLayout()
        self.npropADB = QPushButton("Add Property")
        self.npropCB = QPushButton("Cancel")
        self.npropCB.clicked.connect(self.cancel)
        self.npropR.addWidget(self.npropADB)
        self.npropR.addWidget(self.npropCB)
        self.npropT.addLayout(self.npropR)

    def admin_main(self):
        self.stacked_widget.setCurrentIndex(8) 
        self.adminMainT = QVBoxLayout()
        self.adminMainT.addWidget((QLabel("Welcome")))
        self.aViewVisit = QPushButton("View Visitors List")
        self.adminMainT.addWidget(self.aViewVisit)
        self.aViewVisit.clicked.connect(self.a_visitor())
        self.aViewOwner = QPushButton("View Owners List")
        self.adminMainT.addWidget(self.aViewOwner)
        self.aViewOwner.clicked.connect(self.a_owner())
        self.aViewConfirmed = QPushButton("View Confirmed Properties")
        self.adminMainT.addWidget(self.aViewConfirmed)
        self.aViewConfirmed.clicked.connect(self.a_confirmed())
        self.aViewUnconfirmed = QPushButton("View Unconfirmed Properties")
        self.adminMainT.addWidget(self.aViewUnconfirmed)
        self.aViewUnconfirmed.clicked.connect(self.a_unconfirmed())
        self.aViewApproved = QPushButton("View Approved Animals and Crops")
        self.adminMainT.addWidget(self.aViewApproved)
        self.aViewApproved.clicked.connect(self.a_approved())
        self.aViewPending = QPushButton("View Pending Animals and Crops")
        self.adminMainT.addWidget(self.aViewPending)
        self.aViewPending.clicked.connect(self.a_pending())

    def a_unconfirmed(self):
        self.stacked_widget.setCurrentIndex(9)

    def a_manage(self):
        self.stacked_widget.setCurrentIndex(10)

    def a_confirmed(self):
        self.stacked_widget.setCurrentIndex(11)

    def a_owner(self):
        self.stacked_widget.setCurrentIndex(12)

    def a_visitor(self):
        self.stacked_widget.setCurrentIndex(13)

    def a_pending(self):
        self.stacked_widget.setCurrentIndex(14)

    def a_approved(self):
        self.stacked_widget.setCurrentIndex(15)

    def visitor_main(self):
        self.stacked_widget.setCurrentIndex(16)
        self.visitMainT = QVBoxLayout()

    def v_prop_detail(self):
        self.stacked_widget.setCurrentIndex(17)

    def v_visit_hist(self):
        self.stacked_widget.setCurrentIndex(18)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())