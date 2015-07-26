__author__ = 'taisuke'

import cv2
import numpy as np
from form import Ui_Form
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene


class Visualizer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Visualizer, self).__init__(parent)
        self.file = ''
        self.scene = QGraphicsScene()
        self.ui = Ui_Form()
        self.setupUi(self)

    # imageはopencvのオブジェクト
    def drawImage(self, image):
        height, width, dim = image.shape
        image = QImage(image, width, height, dim * width, QImage.Format_RGB888)
        self.scene = QGraphicsScene()
        self.scene.addItem(QGraphicsPixMapItem(QPixmap.fromImage(image)))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = Visualizer()

    main.show()
    sys.exit(app.exec_())
