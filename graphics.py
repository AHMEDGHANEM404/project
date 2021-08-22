from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt




class Window(QMainWindow):
    def __init__(self,sucesses,Totall):
        super().__init__()

        self.setWindowTitle("العرض")
        self.setGeometry(100,100, 1280,600)

        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.show()
        self.sucesses=sucesses
        self.totall=Totall
        self.fail=self.totall-self.sucesses
        self.create_donutchart(self.sucesses,self.fail)



    def create_donutchart(self,sucess,fail):

        series = QPieSeries()
        series.setHoleSize(0.35)
        series.append(f"Protein {fail}%", fail)
        slice = QPieSlice()
        slice = series.append(f"Fat {fail}%", sucess)
        slice.setExploded()
        slice.setLabelVisible()
        series.append("Other 23.8%", 23.8);
        series.append("Carbs 56.4%", 56.4);





        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("نسب النجاح")
        chart.setTheme(QChart.ChartThemeBlueCerulean)



        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)


        self.setCentralWidget(chartview)







# App = QApplication(sys.argv)
# window = Window()
# sys.exit(App.exec_())