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
    def evaluate(self, max_score, circles, picture_data):
        self.score = max_score
        self.width = picture_data.width
        self.height = picture_data.height
        self.overlap = [[0 for col in range(self.width)] for row in range(self.height)]
        self.drawOverlap(circles)
        for line in self.overlap:
            for pixel in line:
                self.score -= (pixel-1)

        return self.score

    def setOverlap(self, circles):
        for circle in circles:
            self.drawCircle(circle)

    def drawCircle(self, circle):
        left = self.width - circle.radius
        right = self.width + circle.radius
        for x in range(left, right):
            r = circle.radius
            h = math.sqrt(x*x+r*r)
            for y in range(self.height-h, self.height+h):
                self.dot(x,y)

    def dot(self, x, y):
        if x<0 or x>=self.width:
            return
        elif y<0 or y>=self.height:
            return
        self.overlap[y][x] += 1

import Evaluation.PictureData
import utility.Circle

picture_data = Evaluation.PictureData()
picture_data.width = 100
picture_data.height = 100
circles = list()
circles.append(Circle())



