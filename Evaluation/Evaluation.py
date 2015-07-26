# coding: utf-8
__author__ = 'minto'

from Evaluation.SizeEvaluation import SizeEvaluation
from Evaluation.OverlapEvaluation import OverlapEvaluation
from Evaluation.ExposedEvaluation import ExposedEvaluation


class Evaluation:
    """
    水玉の配置の評価を行うためのクラス
    """

    def evaluate(self, circles, picture_data):
        score = 0
        score += SizeEvaluation().evaluate(circles, picture_data)
        score += OverlapEvaluation().evaluate(circles, picture_data)
        score += ExposedEvaluation().evaluate(circles, picture_data)
        return score*0.01
