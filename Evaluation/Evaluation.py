# coding: utf-8
__author__ = 'minto'

from Evaluation.SizeEvaluation import SizeEvaluation


class Evalution:

    def evaluate(self, max_score, circles, picture):
        score = 0
        score += SizeEvaluation().evaluate(10, circles)

        return score
