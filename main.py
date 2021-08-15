from mainUI import Ui_MainWindow
from PyQt5.QtCore import QObject, QSettings, QTimer
from PyQt5.QtGui import QIcon,QTextCursor, QTextDocument
from PyQt5.QtWidgets import (QApplication, QCheckBox, QSpinBox, QFileDialog, QLineEdit, QMainWindow,QToolBar,QLabel)

import sys
from .common import *


class SearchIP(Ui_MainWindow,QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = SearchIP()
    main.show()
    sys.exit(app.exec_())