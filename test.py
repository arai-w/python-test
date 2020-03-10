from PyQt5.QtWidgets import QCalendarWidget, QApplication
from PyQt5.QtCore import QDate

def myfunc():
    dt=calendar.selectedDate()
    print(dt)

app = QApplication.instance()
if (app is None):
    app=QApplication([])

calendar = QCalendarWidget()
calendar.setGridVisible(True)
calendar.setGeometry(600,400,450,350)
calendar.setWindowTitle("日付選択")

calendar.clicked[QDate].connect(myfunc)

calendar.show()
app.exec_()