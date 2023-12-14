import sys
import re
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_plikZapisz.clicked.connect(self.getOsobaData)
        self.ui.pushButton_zapisz.clicked.connect(self.dodajPlik)
        self.show()

    def isPeselValid(self, pesel):
        return re.match(r'^[0-9]{11}$', pesel) is not None

    def getOsobaData(self):
        imie = self.ui.lineEdit_imie.text()
        nazwisko = self.ui.lineEdit_nazwisko.text()
        pesel = self.ui.lineEdit_pesel.text()
        nrTel = self.ui.lineEdit_tel.text()

        dane = f"{imie} {nazwisko}"
    def dodajPlik(self):
        imie = self.ui.lineEdit_imie.text()
        nazwisko = self.ui.lineEdit_nazwisko.text()
        pesel = self.ui.lineEdit_pesel.text()
        tel = self.ui.lineEdit_tel.text()

        dane = f"{imie} {nazwisko}"
        employees_file = f"{imie}_{nazwisko}.txt"

        if self.isPeselValid(pesel):
            with open(employees_file, 'a') as file:
                file.write(f"{dane}\n")
            self.ui.listWidget_praco.addItem(f"{imie} {nazwisko}")
        else:
            crash = QMessageBox()
            crash.setText("pesel nie jest poprawny")
            crash.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
