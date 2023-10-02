# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowAquaPlanet.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_AquaPlanetMain(object):
    def setupUi(self, AquaPlanetMain):
        AquaPlanetMain.setObjectName("AquaPlanetMain")
        AquaPlanetMain.setWindowModality(QtCore.Qt.NonModal)
        AquaPlanetMain.resize(480, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AquaPlanetMain.sizePolicy().hasHeightForWidth())
        AquaPlanetMain.setSizePolicy(sizePolicy)
        AquaPlanetMain.setMinimumSize(QtCore.QSize(480, 320))
        AquaPlanetMain.setMaximumSize(QtCore.QSize(480, 320))
        AquaPlanetMain.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(AquaPlanetMain)
        self.centralwidget.setObjectName("centralwidget")
        self.diplayHumedad = QtWidgets.QLCDNumber(self.centralwidget)
        self.diplayHumedad.setGeometry(QtCore.QRect(30, 60, 131, 51))
        self.diplayHumedad.setObjectName("diplayHumedad")
        self.displayTemp = QtWidgets.QLCDNumber(self.centralwidget)
        self.displayTemp.setGeometry(QtCore.QRect(260, 60, 131, 51))
        self.displayTemp.setObjectName("displayTemp")
        self.labelPorcentaje = QtWidgets.QLabel(self.centralwidget)
        self.labelPorcentaje.setGeometry(QtCore.QRect(170, 50, 41, 71))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.labelPorcentaje.setFont(font)
        self.labelPorcentaje.setObjectName("labelPorcentaje")
        self.labelGradosC = QtWidgets.QLabel(self.centralwidget)
        self.labelGradosC.setGeometry(QtCore.QRect(400, 50, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.labelGradosC.setFont(font)
        self.labelGradosC.setObjectName("labelGradosC")
        self.labelHumedad = QtWidgets.QLabel(self.centralwidget)
        self.labelHumedad.setGeometry(QtCore.QRect(30, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelHumedad.setFont(font)
        self.labelHumedad.setObjectName("labelHumedad")
        self.labelTemperatura = QtWidgets.QLabel(self.centralwidget)
        self.labelTemperatura.setGeometry(QtCore.QRect(260, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelTemperatura.setFont(font)
        self.labelTemperatura.setObjectName("labelTemperatura")
        self.botonEncendido = QtWidgets.QPushButton(self.centralwidget)
        self.botonEncendido.setGeometry(QtCore.QRect(180, 190, 101, 91))
        self.botonEncendido.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.botonEncendido.setObjectName("botonEncendido")
        self.nivelTanque = QtWidgets.QProgressBar(self.centralwidget)
        self.nivelTanque.setGeometry(QtCore.QRect(390, 180, 41, 121))
        self.nivelTanque.setStyleSheet("")
        self.nivelTanque.setProperty("value", 25)
        self.nivelTanque.setTextVisible(False)
        self.nivelTanque.setOrientation(QtCore.Qt.Vertical)
        self.nivelTanque.setObjectName("nivelTanque")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.OnOff = QtWidgets.QLabel(self.centralwidget)
        self.OnOff.setGeometry(QtCore.QRect(140, 130, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.OnOff.setFont(font)
        self.OnOff.setObjectName("OnOff")
        self.iconoNube = QtWidgets.QLabel(self.centralwidget)
        self.iconoNube.setGeometry(QtCore.QRect(10, 219, 100, 80))
        self.iconoNube.setStyleSheet("image: url(:/iconoNubeBlanco/g982.png);")
        self.iconoNube.setText("")
        self.iconoNube.setObjectName("iconoNube")
        self.Backgraund = QtWidgets.QLabel(self.centralwidget)
        self.Backgraund.setGeometry(QtCore.QRect(60, 10, 341, 301))
        self.Backgraund.setStyleSheet("image: url(:/iconogotamas/g107.png);")
        self.Backgraund.setText("")
        self.Backgraund.setObjectName("Backgraund")

        self.label_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_gif.setGeometry(QtCore.QRect(20, 120, 91, 91))
        self.movie = QMovie(":/gif/gota-agua.gif")
        self.movie.setScaledSize(QtCore.QSize(90,90))
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        self.label_gif.raise_()

        self.Backgraund.raise_()
        self.diplayHumedad.raise_()
        self.displayTemp.raise_()
        self.labelPorcentaje.raise_()
        self.labelGradosC.raise_()
        self.labelHumedad.raise_()
        self.labelTemperatura.raise_()
        self.botonEncendido.raise_()
        self.nivelTanque.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.OnOff.raise_()
        self.iconoNube.raise_()
        AquaPlanetMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(AquaPlanetMain)
        QtCore.QMetaObject.connectSlotsByName(AquaPlanetMain)

    def retranslateUi(self, AquaPlanetMain):
        _translate = QtCore.QCoreApplication.translate
        AquaPlanetMain.setWindowTitle(_translate("AquaPlanetMain", "MainWindow"))
        self.labelPorcentaje.setText(_translate("AquaPlanetMain", "%"))
        self.labelGradosC.setText(_translate("AquaPlanetMain", "°C"))
        self.labelHumedad.setText(_translate("AquaPlanetMain", "Humedad"))
        self.labelTemperatura.setText(_translate("AquaPlanetMain", "Temperatura"))
        self.botonEncendido.setText(_translate("AquaPlanetMain", "Lector QR"))
        self.label.setText(_translate("AquaPlanetMain", "Nivel de"))
        self.label_2.setText(_translate("AquaPlanetMain", "Tanque"))
        self.OnOff.setText(_translate("AquaPlanetMain", "<html><head/><body><p align=\"center\">Reposo</p></body></html>"))
import icons.iconos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AquaPlanetMain = QtWidgets.QMainWindow()
    ui = Ui_AquaPlanetMain()
    ui.setupUi(AquaPlanetMain)
    AquaPlanetMain.show()
    sys.exit(app.exec_())