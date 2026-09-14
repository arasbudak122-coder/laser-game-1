
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("github link")
        Dialog.resize(400, 300)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 0, 351, 51))
        self.commandLinkButton.setObjectName("commandLinkButton")
        # Butona basılınca GitHub linkini aç
        self.commandLinkButton.clicked.connect(
            lambda: QtGui.QDesktopServices.openUrl(
                QtCore.QUrl("https://github.com/arasbudak122-coder/laser-game-1")
            )
        )
        self.checkBox = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 171, 51))
        self.checkBox.setObjectName("checkBox")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(
            _translate("Github Link", "Github link")
        )
        self.commandLinkButton.setText(
            _translate(
                "Dialog",
                "https://github.com/arasbudak122-coder/laser-game-1"
            )
        )
        self.checkBox.setText(
            _translate(
                "Dialog",
                "Can You love it my link"
            )
        )
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())                                                                                                    
