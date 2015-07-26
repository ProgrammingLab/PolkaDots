# coding: utf-8

"""
円の大きさのバラバラさによる評価
"""


class SizeEvaluation:

    def __init__(self):
        self.score = 0

    def evaluate(self,circles, picture_data):
        var = float(self.variance(circles))
        return var

    def variance(self, circles):
        ave = self.average(circles)
        var = 0.0
        for circle in circles:
            var += pow(circle.radius - ave, 2)
        return var/len(circles)

    def average(self, circles):
        radius_sum = 0.0
        for circle in circles:
            radius_sum += circle.radius
        return radius_sum / len(circles)