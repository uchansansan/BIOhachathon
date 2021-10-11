import design2 as design
import sys
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sequence = 0
        self.site = 0
        self.setStyleSheet("background-color: #e0cdbe;")

    def SaveSeq(self):
        if self.pushButton.isChecked():
            #self.label_2.setText(self.lineEdit.text())
            self.sequence = self.lineEdit.text()
            self.textBrowser.append(self.sequence)

    def SaveSite(self):
        if self.pushButton_2.isChecked():
            #self.label.setText(self.lineEdit_2.text())
            self.site = self.lineEdit_2.text()
            self.textBrowser.append(self.site)


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
