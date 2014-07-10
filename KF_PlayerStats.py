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
        Dialog.setMinimumSize(QtCore.QSize(649, 461))
        Dialog.setMaximumSize(QtCore.QSize(649, 461))
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
        self.textEdit_1.setReadOnly(True)
        self.tabs.addTab(self.tab_1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.tabs.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_3 = QtGui.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setReadOnly(True)
        self.tabs.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_4 = QtGui.QTextEdit(self.tab_4)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setReadOnly(True)
        self.tabs.addTab(self.tab_4, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit_5 = QtGui.QTextEdit(self.tab_5)
        self.textEdit_5.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setReadOnly(True)
        self.tabs.addTab(self.tab_5, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.textEdit_6 = QtGui.QTextEdit(self.tab_6)
        self.textEdit_6.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_6.setReadOnly(True)
        self.tabs.addTab(self.tab_6, "")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.textEdit_7 = QtGui.QTextEdit(self.tab_7)
        self.textEdit_7.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_7.setReadOnly(True)
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
        if readSteamID == '':
            noSteamID = 1
        else:
            noSteamID = 0
        sUrl = "http://steamcommunity.com/id/" + readSteamID + "/statsfeed/1250?xml=1&schema=1&l=english"
        page = urlopen(sUrl)
        string = page.read()
        root = etree.fromstring(string)

        eN = 0
        parsedErrorTag = [None] * 3
        parsedErrorText = [None] * 3
        for e in root:
            parsedErrorTag[eN] = e.tag
            parsedErrorText[eN] = e.text
            eN = eN + 1

        if noSteamID == 1:
            errorString = str('<br><font color="red"><b>YOU MUST ENTER A VALID STEAM ID!!</font><b>')
            self.textEdit_1.setHtml(errorString.upper())
            self.textEdit_2.setHtml(errorString.upper())
            self.textEdit_3.setHtml(errorString.upper())
            self.textEdit_4.setHtml(errorString.upper())
            self.textEdit_5.setHtml(errorString.upper())
            self.textEdit_6.setHtml(errorString.upper())
            self.textEdit_7.setHtml(errorString.upper())
        elif parsedErrorTag[0] == "error":
            errorString = str('<br><font color="red"><b>' + parsedErrorTag[0] + ": " + parsedErrorText[0] + '</font><b>')
            self.textEdit_1.setHtml(errorString.upper())
            self.textEdit_2.setHtml(errorString.upper())
            self.textEdit_3.setHtml(errorString.upper())
            self.textEdit_4.setHtml(errorString.upper())
            self.textEdit_5.setHtml(errorString.upper())
            self.textEdit_6.setHtml(errorString.upper())
            self.textEdit_7.setHtml(errorString.upper())
        elif parsedErrorTag[1] == "error":
            errorString = str('<br><font color="red"><b>' + parsedErrorTag[1] + ": " + parsedErrorText[1] + '</font><b>')
            self.textEdit_1.setHtml(errorString.upper())
            self.textEdit_2.setHtml(errorString.upper())
            self.textEdit_3.setHtml(errorString.upper())
            self.textEdit_4.setHtml(errorString.upper())
            self.textEdit_5.setHtml(errorString.upper())
            self.textEdit_6.setHtml(errorString.upper())
            self.textEdit_7.setHtml(errorString.upper())
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

            totalKills = int(parsedStat[0])
            damageHealed = int(parsedStat[1])
            weldingPoints = int(parsedStat[2])
            shotgunDamage = int(parsedStat[3])
            headshotKills = int(parsedStat[4])
            stalkerKills = int(parsedStat[5])
            bullpupDamage = int(parsedStat[6])
            meleeDamage = int(parsedStat[7])
            flamethrowerDamage = int(parsedStat[8])
            explosivesDamage = int(parsedStat[20])
            totalKills = str('{0:,}'.format(totalKills))
            damageHealed_S = str('{0:,}'.format(damageHealed))
            weldingPoints_S = str('{0:,}'.format(weldingPoints))
            shotgunDamage_S = str('{0:,}'.format(shotgunDamage))
            headshotKills_S = str('{0:,}'.format(headshotKills))
            stalkerKills_S = str('{0:,}'.format(stalkerKills))
            bullpupDamage_S = str('{0:,}'.format(bullpupDamage))
            meleeDamage_S = str('{0:,}'.format(meleeDamage))
            flamethrowerDamage_S = str('{0:,}'.format(flamethrowerDamage))
            explosivesDamage_S = str('{0:,}'.format(explosivesDamage))

            if damageHealed >= 100000:
                medicLevel = 6
                damageHealedToLevel = 0
            elif damageHealed >= 25000:
                medicLevel = 5
                damageHealedToLevel = (100000 - damageHealed)
            elif damageHealed >= 12000:
                medicLevel = 4
                damageHealedToLevel = (25000 - damageHealed)
            elif damageHealed >= 4000:
                medicLevel = 3
                damageHealedToLevel = (12000 - damageHealed)
            elif damageHealed >= 750:
                medicLevel = 2
                damageHealedToLevel = (4000 - damageHealed)
            elif damageHealed >= 200:
                medicLevel = 1
                damageHealedToLevel = (750 - damageHealed)
            else:
                medicLevel = 0
                damageHealedToLevel = (200 - damageHealed)
            if damageHealedToLevel < 0:
                damageHealedToLevel = 0
            damageHealedToLevel_S = '{0:,}'.format(damageHealedToLevel)

            if weldingPoints >= 370000 and shotgunDamage >= 5500000:
                supportLevel = 6
                weldingPointsToLevel = 0
                shotgunDamageToLevel = 0
            elif weldingPoints >= 250000 and shotgunDamage >= 3500000:
                supportLevel = 5
                weldingPointsToLevel = (370000 - weldingPoints)
                shotgunDamageToLevel = (5500000 - shotgunDamage)
            elif weldingPoints >= 120000 and shotgunDamage >= 1500000:
                supportLevel = 4
                weldingPointsToLevel = (250000 - weldingPoints)
                shotgunDamageToLevel = (3500000 - shotgunDamage)
            elif weldingPoints >= 35000 and shotgunDamage >= 500000:
                supportLevel = 3
                weldingPointsToLevel = (120000 - weldingPoints)
                shotgunDamageToLevel = (1500000 - shotgunDamage)
            elif weldingPoints >= 7000 and shotgunDamage >= 100000:
                supportLevel = 2
                weldingPointsToLevel = (35000 - weldingPoints)
                shotgunDamageToLevel = (500000 - shotgunDamage)
            elif weldingPoints >= 2000 and shotgunDamage >= 25000:
                supportLevel = 1
                weldingPointsToLevel = (7000 - weldingPoints)
                shotgunDamageToLevel = (100000 - shotgunDamage)
            else:
                supportLevel = 0
                weldingPointsToLevel = (2000 - weldingPoints)
                shotgunDamageToLevel = (25000 - shotgunDamage)
            if weldingPointsToLevel < 0:
                weldingPointsToLevel = 0
            if shotgunDamageToLevel < 0:
                shotgunDamageToLevel = 0
            weldingPointsToLevel_S = '{0:,}'.format(weldingPointsToLevel)
            shotgunDamageToLevel_S = '{0:,}'.format(shotgunDamageToLevel)

            if bullpupDamage >= 5500000 and stalkerKills >= 3600:
                commandoLevel = 6
                bullpupDamageToLevel = 0
                stalkerKillsToLevel = 0
            elif bullpupDamage >= 3500000 and stalkerKills >= 2400:
                commandoLevel = 5
                bullpupDamageToLevel = (5500000 - bullpupDamage)
                stalkerKillsToLevel = (3600 - stalkerKills)
            elif bullpupDamage >= 1500000 and stalkerKills >= 1200:
                commandoLevel = 4
                bullpupDamageToLevel = (3500000 - bullpupDamage)
                stalkerKillsToLevel = (2400 - stalkerKills)
            elif bullpupDamage >= 500000 and stalkerKills >= 350:
                commandoLevel = 3
                bullpupDamageToLevel = (1500000 - bullpupDamage)
                stalkerKillsToLevel = (1200 - stalkerKills)
            elif bullpupDamage >= 100000 and stalkerKills >= 100:
                commandoLevel = 2
                bullpupDamageToLevel = (500000 - bullpupDamage)
                stalkerKillsToLevel = (350 - stalkerKills)
            elif bullpupDamage >= 25000 and stalkerKills >= 30:
                commandoLevel = 1
                bullpupDamageToLevel = (100000 - bullpupDamage)
                stalkerKillsToLevel = (100 - stalkerKills)
            else:
                commandoLevel = 0
                bullpupDamageToLevel = (25000 - bullpupDamage)
                stalkerKillsToLevel = (30 - stalkerKills)
            if bullpupDamageToLevel < 0:
                bullpupDamageToLevel = 0
            if stalkerKillsToLevel < 0:
                stalkerKillsToLevel = 0
            bullpupDamageToLevel_S = '{0:,}'.format(bullpupDamageToLevel)
            stalkerKillsToLevel_S = '{0:,}'.format(stalkerKillsToLevel)

            if meleeDamage >= 5500000:
                berserkerLevel = 6
                meleeDamageToLevel = 0
            elif meleeDamage >= 3500000:
                berserkerLevel = 5
                meleeDamageToLevel = (5500000 - meleeDamage)
            elif meleeDamage >= 1500000:
                berserkerLevel = 4
                meleeDamageToLevel = (3500000 - meleeDamage)
            elif meleeDamage >= 500000:
                berserkerLevel = 3
                meleeDamageToLevel = (1500000 - meleeDamage)
            elif meleeDamage >= 100000:
                berserkerLevel = 2
                meleeDamageToLevel = (500000 - meleeDamage)
            elif meleeDamage >= 25000:
                berserkerLevel = 1
                meleeDamageToLevel = (100000 - meleeDamage)
            else:
                berserkerLevel = 0
                meleeDamageToLevel = (25000 - meleeDamage)
            if meleeDamageToLevel < 0:
                meleeDamageToLevel = 0
            meleeDamageToLevel_S = '{0:,}'.format(meleeDamageToLevel)

            if headshotKills >= 8500:
                sharpshooterLevel = 6
                headshotKillsToLevel = 0
            elif headshotKills >= 5500:
                sharpshooterLevel = 5
                headshotKillsToLevel = (8500 - headshotKills)
            elif headshotKills >= 2500:
                sharpshooterLevel = 4
                headshotKillsToLevel = (5500 - headshotKills)
            elif headshotKills >= 700:
                sharpshooterLevel = 3
                headshotKillsToLevel = (2500 - headshotKills)
            elif headshotKills >= 100:
                sharpshooterLevel = 2
                headshotKillsToLevel = (700 - headshotKills)
            elif headshotKills >= 30:
                sharpshooterLevel = 1
                headshotKillsToLevel = (100 - headshotKills)
            else:
                sharpshooterLevel = 0
                headshotKillsToLevel = (30 - headshotKills)
            if headshotKillsToLevel < 0:
                headshotKillsToLevel = 0
            headshotKillsToLevel_S = '{0:,}'.format(headshotKillsToLevel)

            if flamethrowerDamage >= 5500000:
                firebugLevel = 6
                flamethrowerDamageToLevel = 0
            elif flamethrowerDamage >= 3500000:
                firebugLevel = 5
                flamethrowerDamageToLevel = (5500000 - flamethrowerDamage)
            elif flamethrowerDamage >= 1500000:
                firebugLevel = 4
                flamethrowerDamageToLevel = (3500000 - flamethrowerDamage)
            elif flamethrowerDamage >= 500000:
                firebugLevel = 3
                flamethrowerDamageToLevel = (1500000 - flamethrowerDamage)
            elif flamethrowerDamage >= 100000:
                firebugLevel = 2
                flamethrowerDamageToLevel = (500000 - flamethrowerDamage)
            elif flamethrowerDamage >= 25000:
                firebugLevel = 1
                flamethrowerDamageToLevel = (100000 - flamethrowerDamage)
            else:
                firebugLevel = 0
                flamethrowerDamageToLevel = (25000 - flamethrowerDamage)
            if flamethrowerDamageToLevel < 0:
                flamethrowerDamageToLevel = 0
            flamethrowerDamageToLevel_S = '{0:,}'.format(flamethrowerDamageToLevel)

            if explosivesDamage >= 5500000:
                demolitionLevel = 6
                explosivesDamageToLevel = 0
            elif explosivesDamage >= 3500000:
                demolitionLevel = 5
                explosivesDamageToLevel = (5500000 - explosivesDamage)
            elif explosivesDamage >= 1500000:
                demolitionLevel = 4
                explosivesDamageToLevel = (3500000 - explosivesDamage)
            elif explosivesDamage >= 500000:
                demolitionLevel = 3
                explosivesDamageToLevel = (1500000 - explosivesDamage)
            elif explosivesDamage >= 100000:
                demolitionLevel = 2
                explosivesDamageToLevel = (500000 - explosivesDamage)
            elif explosivesDamage >= 25000:
                demolitionLevel = 1
                explosivesDamageToLevel = (100000 - explosivesDamage)
            else:
                demolitionLevel = 0
                explosivesDamageToLevel = (25000 - explosivesDamage)
            if explosivesDamageToLevel < 0:
                explosivesDamageToLevel = 0
            explosivesDamageToLevel_S = '{0:,}'.format(explosivesDamageToLevel)

            if medicLevel < 6:
                self.textEdit_1.setHtml('<b>Medic Level: ' + str(medicLevel) + '<br><br></b><u>For level ' + str((medicLevel) + 1) + ':</u><br>Healing Done Needed: ' + str(damageHealedToLevel_S))
            else:
                self.textEdit_1.setHtml('<b>Medic Level: ' + str(medicLevel) + '<br><br></b><u>Total:</u><br>Kills: ' + totalKills + '<br>Healing Done Total: ' + str(damageHealed_S))
            if supportLevel < 6:
                if shotgunDamageToLevel == 0:
                    self.textEdit_2.setHtml('<b>Support Level: ' + str(supportLevel) + '<br><br></b><u>For level ' + str((supportLevel) + 1) + ':</u><br>Welding Points Needed: ' + str(weldingPointsToLevel_S))
                elif weldingPointsToLevel == 0:
                    self.textEdit_2.setHtml('<b>Support Level: ' + str(supportLevel) + '<br><br></b><u>For level ' + str((supportLevel) + 1) + ':</u><br>Shotgun Damage Needed: ' + str(shotgunDamageToLevel_S))
                else:
                    self.textEdit_2.setHtml('<b>Support Level: ' + str(supportLevel) + '<br><br></b><u>For level ' + str((supportLevel) + 1) + ':</u><br>Shotgun Damage Needed: ' + str(shotgunDamageToLevel_S) + '<br>Welding Points Needed: ' + str(weldingPointsToLevel_S))
            else:
                self.textEdit_2.setHtml('<b>Support Level: ' + str(supportLevel) + '<br><br></b><u>Total:</u><br>Kills: ' + totalKills + '<br>Shotgun Damage Total: ' + str(shotgunDamage_S) + '<br>Welding Points: ' + str(weldingPoints_S))
            if commandoLevel < 6:
                if bullpupDamageToLevel == 0:
                    self.textEdit_3.setHtml('<b>Commando Level: ' + str(commandoLevel) + '<br><br></b><u>For level ' + str((commandoLevel) + 1) + ':</u><br>Stalkers Killed Needed: ' + str(stalkerKillsToLevel_S))
                elif stalkerKillsToLevel == 0:
                    self.textEdit_3.setHtml('<b>Commando Level: ' + str(commandoLevel) + '<br><br></b><u>For level ' + str((commandoLevel) + 1) + ':</u><br>Assault Rifle Damage Needed: ' + str(bullpupDamageToLevel_S))
                else:
                    self.textEdit_3.setHtml('<b>Commando Level: ' + str(commandoLevel) + '<br><br></b><u>For level ' + str((commandoLevel) + 1) + ':</u><br>Assault Rifle Damage Needed: ' + str(bullpupDamageToLevel_S) + '<br>Stalkers Killed Needed: ' + str(stalkerKillsToLevel_S))
            else:
                self.textEdit_3.setHtml('<b>Commando Level: ' + str(commandoLevel) + '<br><br></b><u>Total:</u><br>Kills: ' + totalKills + '<br>Assault Rifle Damage Total: ' + str(bullpupDamage_S) + '<br>Stalkers Killed: ' + str(stalkerKills_S))
            if berserkerLevel < 6:
                self.textEdit_4.setHtml('<b>Berserker Level: ' + str(berserkerLevel) + '<br><br></b><u>For level ' + str((berserkerLevel) + 1) + ':</u><br>Melee Damage Needed: ' + str(meleeDamageToLevel_S))
            else:
                self.textEdit_4.setHtml('<b>Berserker Level: ' + str(berserkerLevel) + '<br><br></b><u>Total:</u><br>Kills: ' + totalKills + '<br>Melee Damage Total: ' + str(meleeDamage_S))
            if sharpshooterLevel < 6:
                self.textEdit_5.setHtml('<b>Sharpshooter Level: ' + str(sharpshooterLevel) + '<br><br></b><u>For level ' + str((sharpshooterLevel) + 1) + ':</u><br>Headshot Kills Needed: ' + str(headshotKillsToLevel_S))
            else:
                self.textEdit_5.setHtml('<b>Sharpshooter Level: ' + str(sharpshooterLevel) + '<br><br></b><u>Total:</u><br>Kills: ' + totalKills + '<br>Headshot Kills Total: ' + str(headshotKills_S))
            if firebugLevel < 6:
                self.textEdit_6.setHtml('<b>Firebug Level: ' + str(firebugLevel) + '<br><br></b><u>For level ' + str((firebugLevel) + 1) + ':</u><br>Flamethrower Damage Needed: ' + str(flamethrowerDamageToLevel_S))
            else:
                self.textEdit_6.setHtml('<b>Firebug Level: ' + str(firebugLevel) + '<br><br></b><u>Total:</u><br>Kills: ' + totalKills + '<br>Flamethrower Damage Total: ' + str(flamethrowerDamage_S))
            if demolitionLevel < 6:
                self.textEdit_7.setHtml('<b>Demolition Level: ' + str(demolitionLevel) + '<br><br></b><u>For level ' + str((demolitionLevel) + 1) + ':</u><br>Explosives Damage Needed: ' + str(explosivesDamageToLevel_S))
            else:
                self.textEdit_7.setHtml('<b>Demolition Level: ' + str(demolitionLevel) + '<br><br></b><u>Total:</u><br>Kills: ' + totalKills + '<br>Explosive Damage Total: ' + str(explosivesDamage_S))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec_()) 
