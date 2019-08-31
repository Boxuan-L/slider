import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QPainter, QImage
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
    
      label = QLabel('Scary', self)
      label.move(370,530)
      
      label = QLabel('cozy', self)
      label.move(600,530)

      sld = QSlider(Qt.Horizontal, self)
      sld.setFocusPolicy(Qt.NoFocus)
      sld.setGeometry(450, 520, 100, 30)
      sld.valueChanged[int].connect(self.changeValue)

      self.label = QLabel(self)
      self.label.setPixmap(QPixmap('Images\\0.jpg'))
      self.label.setGeometry(160, 20, 800, 500)

      self.setGeometry(300, 300, 1000, 600)
      self.setWindowTitle('Slider')
      self.show()

    
    def changeValue(self, value):

      img0 = QImage('Images\\'+ "0.jpg")
      img1 = QImage('Images\\'+ "10.jpg")
      
      painter = QPainter()
      painter.begin(img0)
      painter.setOpacity(value/100)
      painter.drawImage(0,0,img1)
      painter.end()

      self.label.setPixmap(QPixmap.fromImage(img0))

if __name__ == '__main__':

  app = QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())
