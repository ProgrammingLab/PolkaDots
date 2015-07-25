# coding: utf-8
__author__ = 'minto'

from Evaluation.SizeEvaluation import SizeEvaluation
from Evaluation.OverlapEvaluation import OverlapEvaluation


class Evaluation:
    """
    水玉の配置の評価を行うためのクラス
    """


    def evaluate(self, max_score, circles, picture_data):
        score = 0
        score += SizeEvaluation().evaluate(10, circles, picture_data)
        score += OverlapEvaluation().evaluate(10, circles, picture_data)
        return score
