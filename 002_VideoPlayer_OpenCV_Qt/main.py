
import os
import sys
os.system('pyuic5 gui_main/gui_main.ui > gui_main/gui_main.py')
sys.path.append('.')
from gui_main import Ui_Form
from PyQt5 import  QtWidgets
import cv2

#
print(sys.path)
# from gui_main import Ui_Form
# from  PyQt5.QtCore import QObject ,QTimer
# from  PyQt5.QtCore import QThreadPool ,QRunnable ,pyqtSlot
from PyQt5.QtWidgets import  QApplication , QGraphicsScene ,QMainWindow


class appWin(QMainWindow):
    def __init__(self):

        super(appWin, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.graphicsView.setScene(QGraphicsScene(self))
        cap = cv2.VideoCapture('video_file_path.avi')

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret is True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        # self.ui.
        # self.ui.



if __name__ == '__main__':
    app= QApplication(sys.argv)
    win= appWin()
    win.show()
    sys.exit(app.exec())
