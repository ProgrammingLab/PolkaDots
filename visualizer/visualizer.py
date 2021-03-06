__author__ = 'taisuke'

import cv2
import numpy as np
from form import Ui_Form
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene, QFileDialog, QGraphicsPixmapItem


class Visualizer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Visualizer, self).__init__(parent)
        self.file = ''
        self.scene = QGraphicsScene()
        self.ui = Ui_Form()
        self.setupUi(self)

        self.fileSelect.clicked.connect(self.fileSelected)

    # imageはopencvのオブジェクト
    def drawImage(self, image):
        height, width, dim = image.shape
        image = QImage(image, width, height, dim * width, QImage.Format_RGB888)
        image_item = QGraphicsPixmapItem(QPixmap.fromImage(image))
        self.scene = QGraphicsScene()

        __width = image_item.boundingRect().width()
        __height = image_item.boundingRect().height()
        self.graphicsResize(__width, __height)

        self.scene.addItem(image_item)
        self.imageView.setScene(self.scene)

    def graphicsResize(self, width, height):
        __x = self.imageView.x()
        __y = self.imageView.y()

        self.imageView.setGeometry(QRect(__x, __y, width, height))
        __main_x = max(int(__x + width + 10), 630)
        __main_y = int(__y + height + 10)
        self.resize(__main_x, __main_y)

    def fileSelected(self):
        file = QFileDialog.getOpenFileName()
        if file[0]:
            self.file = file[0]
            self.fileEdit.setText(self.file)
            image = cv2.imread(self.file)
            self.drawImage(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = Visualizer()

    main.show()
    sys.exit(app.exec_())
