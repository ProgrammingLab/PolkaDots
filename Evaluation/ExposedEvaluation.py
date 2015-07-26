__author__ = 'minto'

from Evaluation.Overlap import Overlap


class ExposedEvaluation:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.picture = [[]]
        self.overlap = [[]]

    def evaluate(self, circles, picture_data):
        self.picture = picture_data
        self.width = picture_data.width
        self.height = picture_data.height
        self.overlap = Overlap().lap(circles, self.width, self.height)
        score = 0
        for y in range(self.height):
            for x in range(self.width):
                score += self.evalutePoint(x, y)
        return score

    def evalutePoint(self, x, y):
        # x yでその点は露出すべきか否かで点数を返す
        if self.picture.mustExposed(x, y):
            # 露出すべき場所を隠している
            if self.overlap[y][x]==0:
                return 0
            # 露出すべき場所をさらけ出している
            else:
                return 10
        else:
            # 隠すべき場所を隠している
            if self.overlap[y][x]==0:
                return 100
            # 隠すべき場所を露出している
            else:
                return -1000



