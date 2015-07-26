__author__ = 'minto'
import math


class Overlap:

    def lap(self, circles, width, height):
        self.width = width
        self.height = height
        self.data = [[0 for i in range(width)] for k in range(height)]
        self.drawCircles(circles)
        return self.data

    def drawCircles(self, circles):
        for circle in circles:
            self.drawCircle(circle)

    def drawCircle(self, circle):
        left = circle.x - circle.radius
        right = circle.x + circle.radius
        for x in range(left, right):
            r = circle.radius
            xi = circle.x - x
            h = int(math.sqrt(r*r-xi*xi))
            for y in range(circle.y-h, circle.y+h+1):
                self.dot(x, y)

    def dot(self, x, y):
        if x<0 or x>=self.width:
            return
        elif y<0 or y>=self.height:
            return
        self.data[y][x] += 1