# coding: utf-8

import math


class OverlapEvaluation:
    def __init__(self):
        self.score = 0
        self.overlap = []
        self.width = 0
        self.height = 0

    """
    円の重なり具合による評価
        max_score
            int
        circles
            Circle[]
        picture_data
            PictureData
    """
    def evaluate(self,circles, picture_data):
        self.score = 10000
        self.width = picture_data.width
        self.height = picture_data.height
        self.overlap = [[0 for col in range(self.width)] for row in range(self.height)]
        self.setOverlap(circles)
        for line in self.overlap:
            for pixel in line:
                if pixel>1:
                    self.score -= (pixel-1)
        return self.score

    def setOverlap(self, circles):
        for circle in circles:
            self.drawCircle(circle)

    def drawCircle(self, circle):
        left = circle.x - circle.radius
        right = circle.x + circle.radius
        for x in range(left, right+1):
            r = circle.radius
            xi = circle.x - x
            h = int(math.sqrt(r*r-xi*xi))
            for y in range(circle.y-h, circle.y+h+1):
                self.dot(x,y)

    def dot(self, x, y):
        if x<0 or x>=self.width:
            return
        elif y<0 or y>=self.height:
            return
        self.overlap[y][x] += 1


"""
from PictureData import PictureData
from Circle import Circle

picture_data = PictureData()
picture_data.width = 5
picture_data.height = 6
circles = list()
circles.append(Circle(2,0,0))
circles.append(Circle(2,2,2))
overlap = OverlapEvaluation()

print(overlap.evaluate(10, circles, picture_data))
"""



