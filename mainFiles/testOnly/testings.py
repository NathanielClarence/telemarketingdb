'''import pandas as pd

df = pd.read_excel("assets/sample xls/Filenamex.xls", sheet_name= 'Sheet1')
datadict = {}
for x in df:
    #print(x)
    newdat = []
    if x.lower() != 'no':
        for y in df[x]:
            newdat.append(y)
        datadict[x]=newdat
    if x.lower()== 'no hp':
        rows = df.count()[x]
print(datadict)
print(rows)

cntrow = 0

while cntrow < rows:
    newdat = []
    for x in datadict:
        newdat.append(datadict.get(x)[cntrow])
    print(newdat)
    cntrow+=1'''

import os
ss = "kksf"
print(os.getcwd()+"\\"+ss)
if not os.path.exists(os.getcwd()+"\\"+ss):
    os.makedirs(os.getcwd()+"\\"+ss)
    print("created")

'''import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()

        #self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())'''

'''import re

string = "sksksjfa&*&^&**aa aajjss;;;s''sl;;()"
print(''.join(e for e in string if e.isalnum()))
print(re.sub('[^A-Za-z0-9]+', '_', string))'''

'''from PyQt5 import uic, QtWidgets
#from searchHistory import Ui as srcHistory
import datetime
import sys

class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/telleUI.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()
        self.btn_save.setEnabled(True)
        #self.in_recontact.setEnabled(True)
        #self.in_recontact.setDateTime(datetime.datetime.now())
        self.btn_save.clicked.connect(self.save)
        self.in_dob.setMaximumDateTime(datetime.datetime.now())

    def save(self):
        #print()
        print(self.in_dob.dateTime().addDays(1).toString('yyyy-MM-dd'))
        print(self.in_dob.dateTime().addDays(-1).toString('yyyy-MM-dd'))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())'''