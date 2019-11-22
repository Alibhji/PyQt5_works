import os
os.system('pyuic5 main_window.ui > main_window.py')

import sys ,time

from main_window import Ui_MainWindow
from  PyQt5.QtCore import QObject ,QTimer
from  PyQt5.QtCore import QThreadPool ,QRunnable ,pyqtSlot
from PyQt5.QtWidgets import  QApplication ,QMainWindow



class Worker(QRunnable):

    def __init__(self, *args ,**kwargs):
        super(Worker,self).__init__()
        self.args =args
        self.kwargs =kwargs

    @pyqtSlot()
    def run(self):
        print('Thread start.')
        # for i in range(5):
        #     self.args[0].label_2.setText(str(i+1))
        #     time.sleep(1)
        print(self.args , self.kwargs)
        print('Thread have done.')



class appWin(QMainWindow):
    def __init__(self):
        super(appWin, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.threadpool=QThreadPool()
        print('Multithreading with maximum {} thread'.format(self.threadpool.maxThreadCount()))

        self.timer= QTimer()
        self.timer.setInterval(0.1)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start()
        self.count=0


        self.ui.pushButton.clicked.connect(self.on_btn)

    def on_timer_timeout(self):
        self.count+=1;
        self.ui.label.setText(str(self.count))



    def on_btn(self):
        # for i in range(5):
        #     # QApplication.processEvents()
        #     self.ui.label_2.setText(str(i+1))
        #     time.sleep(1)
        worker1=Worker([1,2,3,4] ,'Ali',ui=self.ui,test='pp')
        self.threadpool.start(worker1)



if __name__ == '__main__':
    app= QApplication(sys.argv)
    win= appWin()
    win.show()
    sys.exit(app.exec())







