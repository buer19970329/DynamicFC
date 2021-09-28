import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from code import gui

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainW = QMainWindow()
    ui = gui.Ui_Dialog()
    ui.setupUi(mainW)

    mainW.show()
    sys.exit(app.exec_())
