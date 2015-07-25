# coding: utf-8

"""
円の大きさのバラバラさによる評価
"""


class SizeEvaluation:
    MAX_VARIANCE = 100

    def __init__(self):
        self.score = 0

    def evaluate(self, max_score, circles, picture_data):
        var = float(self.variance(circles))
        if var > self.MAX_VARIANCE:
            return max_score
        else:
            return int(var/self.MAX_VARIANCE*max_score)

    def variance(self, circles):
        ave = self.average(circles)
        var = 0.0
        for circle in circles:
            var += pow(circle - ave, 2)
        return var

    def average(self, circles):
        radius_sum = 0.0
        for circle in circles:
            radius_sum += circle.radius
        return radius_sum / radius_sum
