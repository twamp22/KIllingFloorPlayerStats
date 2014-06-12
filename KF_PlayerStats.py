#!/usr/bin/env python
from lxml import etree
from urllib.request import urlopen
from PyQt4 import QtCore, QtGui
import sys

class Ui_Dialog(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(649, 461)
        self.getStats = QtGui.QPushButton(Dialog)
        self.getStats.setGeometry(QtCore.QRect(5, 5, 90, 25))
        self.getStats.setToolTip("")
        self.getStats.setFlat(False)
        self.getStats.setObjectName("getStats")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 4, 541, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.tabs = QtGui.QTabWidget(Dialog)
        self.tabs.setGeometry(QtCore.QRect(5, 35, 639, 421))
        self.tabs.setAcceptDrops(False)
        self.tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setTabPosition(QtGui.QTabWidget.North)
        self.tabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabs.setElideMode(QtCore.Qt.ElideRight)
        self.tabs.setUsesScrollButtons(False)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(False)
        self.tabs.setObjectName("tabs")
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.textEdit_1 = QtGui.QTextEdit(self.tab_1)
        self.textEdit_1.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_1.setObjectName("textEdit_1")
        self.tabs.addTab(self.tab_1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabs.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_3 = QtGui.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabs.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_4 = QtGui.QTextEdit(self.tab_4)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_4.setObjectName("textEdit_4")
        self.tabs.addTab(self.tab_4, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit_5 = QtGui.QTextEdit(self.tab_5)
        self.textEdit_5.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_5.setObjectName("textEdit_5")
        self.tabs.addTab(self.tab_5, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.textEdit_6 = QtGui.QTextEdit(self.tab_6)
        self.textEdit_6.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_6.setObjectName("textEdit_6")
        self.tabs.addTab(self.tab_6, "")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.textEdit_7 = QtGui.QTextEdit(self.tab_7)
        self.textEdit_7.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_7.setObjectName("textEdit_7")
        self.tabs.addTab(self.tab_7, "")

        self.retranslateUi(Dialog)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Killing Floor Perk Status"))
        self.getStats.setText(_translate("Dialog", "Get Stats"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your SteamID here!", None))
        self.textEdit_1.setHtml(_translate("Dialog", ""))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_1), _translate("Dialog", "Field Medic"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("Dialog", "Support Specialist"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_5), _translate("Dialog", "Sharpshooter"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _translate("Dialog", "Commando"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_4), _translate("Dialog", "Berserker"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_6), _translate("Dialog", "Firebug"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_7), _translate("Dialog", "Demolition"))
        self.getStats.clicked.connect(self.webGetStats)


    def webGetStats(self):
        readSteamID = self.lineEdit.text()
        sUrl = "http://steamcommunity.com/id/" + readSteamID + "/statsfeed/1250?xml=1&schema=1&l=english"
        page = urlopen(sUrl)
        string = page.read()
        root = etree.fromstring(string)

        eN = 0
        parsedErrorTag = [None] * 3
        parsedErrorText = [None] * 3
        for e in root:
            print(eN)
            print (e.tag,"=",e.text)
            parsedErrorTag[eN] = e.tag
            parsedErrorText[eN] = e.text
            eN = eN + 1

        if parsedErrorTag[0] == "error":
            self.textEdit_1.setHtml(parsedErrorTag[0] + ": " + parsedErrorText[0])
            self.textEdit_2.setHtml(parsedErrorTag[0] + ": " + parsedErrorText[0])
            self.textEdit_3.setHtml(parsedErrorTag[0] + ": " + parsedErrorText[0])
            self.textEdit_4.setHtml(parsedErrorTag[0] + ": " + parsedErrorText[0])
            self.textEdit_5.setHtml(parsedErrorTag[0] + ": " + parsedErrorText[0])
            self.textEdit_6.setHtml(parsedErrorTag[0] + ": " + parsedErrorText[0])
            self.textEdit_7.setHtml(parsedErrorTag[0] + ": " + parsedErrorText[0])
        else:
            stats = root[1]
            statslist = list(stats)
            item = stats[1]

            xN = 0
            parsedStat = [None] * 50
            parsedDisplayName = [None] * 50
            for x in stats:
                for i in statslist[xN]:
                    parsedStat[xN] = x[1].text
                    parsedDisplayName[xN] = x[2].text
                xN = xN + 1

            self.textEdit_1.setHtml(parsedDisplayName[1] + ": " + parsedStat[1])
            self.textEdit_2.setHtml(parsedDisplayName[2] + ": " + parsedStat[2] + "<br>" + parsedDisplayName[3] + ": " + parsedStat[3])
            self.textEdit_3.setHtml(parsedDisplayName[4] + ": " + parsedStat[4])
            self.textEdit_4.setHtml(parsedDisplayName[5] + ": " + parsedStat[5] + "<br>" + parsedDisplayName[6] + ": " + parsedStat[6])
            self.textEdit_5.setHtml(parsedDisplayName[7] + ": " + parsedStat[7])
            self.textEdit_6.setHtml(parsedDisplayName[8] + ": " + parsedStat[8])
            self.textEdit_7.setHtml(parsedDisplayName[20] + ": " + parsedStat[20])
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Dialog()
	ex.show()
	sys.exit(app.exec_()) 
