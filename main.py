import sys
import platform
from PyQt5.QtWidgets import QApplication, QProgressBar, QGraphicsDropShadowEffect, QMainWindow, QPushButton, QWidget
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtGui import QColor


counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('splash_screen.ui', self)
        # self.m_ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)
        # self.progress = QProgressBar(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress_show)
        self.timer.start(35)
        self.show()

    def progress_show(self):
        global counter

        # self.progress= QtGui.QProgressBar(self)
        # progressbar.setValue(50)
        # self.progress.setValue(counter)
        
        
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
            # self.
        counter += 1

        # self.progressBar.setValue(counter)
if __name__ == "__main__":
    app = QApplication([])
    window = SplashScreen()
    sys.exit(app.exec_())
