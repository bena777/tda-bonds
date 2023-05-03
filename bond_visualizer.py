from PyQt5 import QtCore, QtGui, QtWidgets
from bond import Bond
from pyqtgraph import PlotWidget, PlotCurveItem
import numpy as np


# Uses PyQt5 to create a bond visualizer using TDA bond data
# All returns are calculated assuming the bond is held until maturity
# Linear model graph is only used for 0 coupon bonds since this it does not work with coupon based assets
# Created by Ben A, 2023

class Ui_BondVisualizer(object):
    def setupUi(self, BondVisualizer):
        BondVisualizer.setObjectName("BondVisualizer")
        BondVisualizer.resize(1000, 700)
        BondVisualizer.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(BondVisualizer)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(250, 0, 450, 91))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.price_labels = QtWidgets.QLabel(self.centralwidget)
        self.price_labels.setGeometry(QtCore.QRect(0, 220, 281, 461))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.price_labels.setFont(font)
        self.price_labels.setObjectName("price_labels")
        self.bond_label = QtWidgets.QLabel(self.centralwidget)
        self.bond_label.setGeometry(QtCore.QRect(120, 90, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bond_label.setFont(font)
        self.bond_label.setStyleSheet("\n"
"background-color: rgb(255, 160, 162);\n"
"border-radius: 15%;")
        self.bond_label.setText("")
        self.bond_label.setObjectName("bond_label")
        self.bond_chart = PlotWidget(self.centralwidget)
        self.bond_chart.setGeometry(QtCore.QRect(540, 210, 461, 491))
        self.bond_chart.setObjectName("bond_chart")
        self.price_output = QtWidgets.QLabel(self.centralwidget)
        self.price_output.setGeometry(QtCore.QRect(110, 222, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        self.price_output.setFont(font)
        self.price_output.setText("")
        self.price_output.setObjectName("price_output")
        self.fv_label = QtWidgets.QLabel(self.centralwidget)
        self.fv_label.setGeometry(QtCore.QRect(190, 300, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        self.fv_label.setFont(font)
        self.fv_label.setText("")
        self.fv_label.setObjectName("fv_label")
        self.coupon_label = QtWidgets.QLabel(self.centralwidget)
        self.coupon_label.setGeometry(QtCore.QRect(150, 390, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        self.coupon_label.setFont(font)
        self.coupon_label.setText("")
        self.coupon_label.setObjectName("coupon_label")
        self.anr_label = QtWidgets.QLabel(self.centralwidget)
        self.anr_label.setGeometry(QtCore.QRect(300, 550, 230, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        self.anr_label.setFont(font)
        self.anr_label.setText("")
        self.anr_label.setObjectName("anr_label")
        self.return_label = QtWidgets.QLabel(self.centralwidget)
        self.return_label.setGeometry(QtCore.QRect(210, 460, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        self.return_label.setFont(font)
        self.return_label.setText("")
        self.return_label.setObjectName("return_label")
        self.dtm_label = QtWidgets.QLabel(self.centralwidget)
        self.dtm_label.setGeometry(QtCore.QRect(290, 620, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        self.dtm_label.setFont(font)
        self.dtm_label.setText("")
        self.dtm_label.setObjectName("dtm_label")
        self.cusip_label = QtWidgets.QLabel(self.centralwidget)
        self.cusip_label.setGeometry(QtCore.QRect(420, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cusip_label.setFont(font)
        self.cusip_label.setObjectName("cusip_label")
        self.cusip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.cusip_input.setGeometry(QtCore.QRect(370, 160, 200, 40))
        self.cusip_input.setText("")
        self.cusip_input.setObjectName("cusip_input")
        font.setPointSize(20)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(150,160,200,40))
        self.start_button.setText("START")
        self.start_button.setObjectName("start_button")
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("\n"
                                      "background-color: rgb(255, 160, 162);\n"
                                      "border-radius: 15%;")
        font.setUnderline(True)
        self.chart_label = QtWidgets.QLabel(self.centralwidget)
        self.chart_label.setGeometry(QtCore.QRect(600,160,400,40))
        self.chart_label.setText("Linear Expected Returns")
        self.chart_label.setObjectName("chart_label")
        self.chart_label.setFont(font)
        self.ack_label = QtWidgets.QLabel(self.centralwidget)
        self.ack_label.setGeometry(QtCore.QRect(0, 0, 250, 50))
        self.ack_label.setObjectName("ack_label")
        BondVisualizer.setCentralWidget(self.centralwidget)
        self.retranslateUi(BondVisualizer)
        def get_data():
            self.cusip = self.cusip_input.text()
            try:
                bond = Bond(self.cusip)
                self.bond_label.setText(bond.get_description())
                self.price_output.setText(str(bond.get_price()))
                self.fv_label.setText(str(bond.get_fv()))
                self.coupon_label.setText(bond.get_coupon()[0])
                self.dtm_label.setText(str(bond.get_dtm()))
                self.return_label.setText(str(bond.get_raw_return().__round__(4))+"%")
                self.anr_label.setText(str(bond.get_ann_return().__round__(4))+"%")
                if float(bond.get_coupon()[0])==0:
                    interpolated_times = np.linspace(0, bond.get_dtm(), 100)
                    interpolated_prices = np.interp(interpolated_times, [0, bond.get_dtm()],[bond.get_price(), bond.get_fv()])
                    curve = PlotCurveItem(interpolated_times, interpolated_prices)
                    self.bond_chart.addItem(curve)
                    self.bond_chart.getAxis("bottom").setLabel(text="Days Passed")
                    self.bond_chart.getAxis("left").setLabel(text="Bond Price")
            except:
                self.bond_label.setText("Invalid input.")
        QtCore.QMetaObject.connectSlotsByName(BondVisualizer)
        self.start_button.clicked.connect(lambda:get_data())
    def retranslateUi(self, BondVisualizer):
        _translate = QtCore.QCoreApplication.translate
        BondVisualizer.setWindowTitle(_translate("BondVisualizer", "MainWindow"))
        self.title_label.setText(_translate("BondVisualizer", "Bond Visualizer"))
        self.price_labels.setText(_translate("BondVisualizer", " Price: \n"
" \n"
" Face Value: \n"
" \n"
" Coupon: \n"
" \n"
" Raw Return: \n"
" \n"
" Annualized Return: \n"
" \n"
" Days Till Maturity: "))
        self.cusip_label.setText(_translate("BondVisualizer", "CUSIP:"))
        self.ack_label.setText(_translate("BondVisualizer", "Created by Ben A using TDA data \n *Chart does NOT work unless bond is 0 coupon"))
        self.cusip_input.setText(_translate("BondVisualizer",""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BondVisualizer = QtWidgets.QMainWindow()
    ui = Ui_BondVisualizer()
    ui.setupUi(BondVisualizer)
    BondVisualizer.show()
    sys.exit(app.exec_())