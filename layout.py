# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1470, 968)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(224, 150, 561, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout = QtWidgets.QFormLayout(self.layoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")
        self.imie_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.imie_label.setObjectName("imie_label")
        self.layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.imie_label)
        self.lineEdit_imie = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_imie.setObjectName("lineEdit_imie")
        self.layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_imie)
        self.nazwisko_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.nazwisko_label.setObjectName("nazwisko_label")
        self.layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nazwisko_label)
        self.lineEdit_nazwisko = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_nazwisko.setObjectName("lineEdit_nazwisko")
        self.layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_nazwisko)
        self.tel_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.tel_label.setObjectName("tel_label")
        self.layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.tel_label)
        self.lineEdit_tel = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_tel)
        self.pesel_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.pesel_label.setObjectName("pesel_label")
        self.layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pesel_label)
        self.lineEdit_pesel = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_pesel.setObjectName("lineEdit_pesel")
        self.layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_pesel)
        self.checkBox_umowa = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBox_umowa.setObjectName("checkBox_umowa")
        self.layout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox_umowa)
        self.pushButton_zapisz = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_zapisz.setObjectName("pushButton_zapisz")
        self.layout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton_zapisz)
        self.listWidget_praco = QtWidgets.QListWidget(parent=self.layoutWidget)
        self.listWidget_praco.setObjectName("listWidget_praco")
        self.layout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.listWidget_praco)
        self.pushButton_plikZapisz = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_plikZapisz.setObjectName("pushButton_plikZapisz")
        self.layout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton_plikZapisz)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.imie_label.setText(_translate("Dialog", "Imie"))
        self.nazwisko_label.setText(_translate("Dialog", "Nazwisko"))
        self.tel_label.setText(_translate("Dialog", "Numer tel"))
        self.pesel_label.setText(_translate("Dialog", "Pesel"))
        self.checkBox_umowa.setText(_translate("Dialog", "Umowa o prace"))
        self.pushButton_zapisz.setText(_translate("Dialog", "Zapisz"))
        self.pushButton_plikZapisz.setText(_translate("Dialog", "Zapisz do pliku"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
