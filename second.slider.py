import sys
import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
    
      label = QLabel('Color', self)
      label.move(370,530)
      
      label2 = QLabel('Brightness', self)
      label2.move(370,580)
      
      label3 = QLabel('View Area', self)
      label3.move(370,630)


      self.sld = QSlider(Qt.Horizontal, self)
      self.sld.setFocusPolicy(Qt.NoFocus)
      self.sld.setGeometry(450, 520, 100, 30)
      self.sld.valueChanged[int].connect(self.changeValue)
      
      self.sld2 = QSlider(Qt.Horizontal, self)
      self.sld2.setFocusPolicy(Qt.NoFocus)
      self.sld2.setGeometry(450, 570, 100, 30)
      self.sld2.valueChanged[int].connect(self.changeValue)
      
      self.sld3 = QSlider(Qt.Horizontal, self)
      self.sld3.setFocusPolicy(Qt.NoFocus)
      self.sld3.setGeometry(450, 620, 100, 30)
      self.sld3.valueChanged[int].connect(self.changeValue)

      self.label = QLabel(self)
      self.label.setPixmap(QPixmap('Images\\'+ '00_scary.jpg'))
      #self.label.setPixmap(QPixmap('C:\\Users\\Administrator\\Desktop\\00_scary.jpg'))
      self.label.setGeometry(160, 20, 800, 500)

      self.setGeometry(300, 200, 1000, 670)
      self.setWindowTitle('Slider')
      self.show()
    
    
    def changeValue(self, value):
        
      BR_value = self.sld.value()
      BD_value = self.sld2.value()
      LH_value = self.sld3.value()

      img1 = QImage('Images\\'+ "00_scary.jpg")
      img0 = QImage('Images\\'+ "01_color.jpg")
      img2 = QImage('Images\\'+ "02_brightness.jpg")
      img3 = QImage('Images\\'+ "03_area.jpg")
      img4 = QImage('Images\\'+ "04_color-brightness.jpg")
      img5 = QImage('Images\\'+ "05_color-area.jpg")
      img6 = QImage('Images\\'+ "06_brightness-area.jpg")
      img7 = QImage('Images\\'+ "07_cosy.jpg")
      
      #Color
      painter = QPainter()
      painter.begin(img0)
      painter.setOpacity(BR_value/100)
      painter.drawImage(0,0,img1)
      painter.end()
      
      #mix color&brightness filter
      painter1 = QPainter()
      painter1.begin(img2)
      painter1.setOpacity(BR_value/100)
      painter1.drawImage(0,0,img4)
      painter1.end()
      
      #Brightness
      painter2 = QPainter()
      painter2.begin(img0)
      painter2.setOpacity(BD_value/100)
      painter2.drawImage(0,0,img2)
      painter2.end()
      
      #mix bright
      painter3 = QPainter()
      painter3.begin(img3)
      painter3.setOpacity(BR_value/100)
      painter3.drawImage(0,0,img5)
      painter3.end()
      
      #mix color
      painter4 = QPainter()
      painter4.begin(img6)
      painter4.setOpacity(BR_value/100)
      painter4.drawImage(0,0,img7)
      painter4.end()
      
      #mix both
      painter5 = QPainter()
      painter5.begin(img3)
      painter5.setOpacity(BD_value/100)
      painter5.drawImage(0,0,img6)
      painter5.end()
      
      #Visual area
      painter5 = QPainter()
      painter5.begin(img0)
      painter5.setOpacity(LH_value/100)
      painter5.drawImage(0,0,img3)
      painter5.end()
      
      #self.label.setPixmap(QPixmap('Images\\' + counter + '.jpg'))
      self.label.setPixmap(QPixmap.fromImage(img0))
if __name__ == '__main__':

  app = QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())
