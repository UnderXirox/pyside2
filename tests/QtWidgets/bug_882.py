from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os

if "DISPLAY" in os.environ:
    del os.environ["DISPLAY"]

app = QApplication([])
QTimer.singleShot(0, app.quit)
app.exec_()



