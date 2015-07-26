# coding: utf-8

from Evaluation.Circle import Circle
from Evaluation.Evaluation import Evaluation
import Evaluation.Evaluation
import random

class Heredity:
    HEREDITY_NUM = 8
    MAX_RADIUS = 100
    CHANGE_NUM = 100
    MUTATION_PROLABILITY = 10

    def __init__(self, picture_data):
        self.width = picture_data.width
        self.height = picture_data.height
        self.picture_data = picture_data

        self.children = []
        self.scores = []
        for i in range(0, self.HEREDITY_NUM):
            self.makeRandomHeredity()
            self.scores.append(0)

    #初期の子作り
    def makeRandomHeredity(self):
        num = random.randint(1,self.HEREDITY_NUM)
        circles = []
        for i in range(0, num):
            radius = random.randint(1, self.MAX_RADIUS)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            circles.append(Circle(radius, x, y))
        self.children.append(circles)

    #遺伝的アルゴリズムで、一番いい親を拾ってくる
    def getExcellent(self):
        for change_i in range(self.CHANGE_NUM):
            print("%s 代目" % change_i)
            s = ""
            for score in self.scores:
                s += str(score) + " "
            print(s)
            for heredity_i in range(self.HEREDITY_NUM):
                self.grading(heredity_i)
            parents = self.findParent()
            self.makeChildren(parents)

    def makeChildren(self, parents):
        p1 = self.children[parents[0]]
        p2 = self.children[parents[1]]

        #子作り
        for i in range(self.HEREDITY_NUM):
            #ランダム交差(親の水玉をランダムに受け継ぐ)
            ps = [x for x in p1]
            for x in p2:
                ps.append(x)
            length = random.randint(5, self.HEREDITY_NUM)
            circles = []
            for k in range(length):
                index = random.randint(0, len(ps)-1)
                circles.append(ps[index])
            self.children[i] = circles

            print("children's circles num" + str(len(self.children[i])))
            #突然変異
            #xの移動
            if random.randint(0,100)<self.MUTATION_PROLABILITY:
                circles = self.children[i]
                c_i = random.randint(0, len(circles)-1)
                self.children[i][c_i].x = random.randint(0, self.picture_data.width)
            #yの移動
            if random.randint(0,100)<self.MUTATION_PROLABILITY:
                circles = self.children[i]
                c_i = random.randint(0, len(circles)-1)
                self.children[i][c_i].y = random.randint(0, self.picture_data.height)

            #半径の変異
            if random.randint(0,100)<self.MUTATION_PROLABILITY:
                circles = self.children[i]
                c_i = random.randint(0, len(circles)-1)
                self.children[i][c_i].y = random.randint(0, self.MAX_RADIUS)

            #子の追加
            if random.randint(0,100)<self.MUTATION_PROLABILITY:
                print("add child")
                if len(self.children[i])<self.HEREDITY_NUM:
                    radius = random.randint(1, self.MAX_RADIUS)
                    x = random.randint(0, self.width)
                    y = random.randint(0, self.height)
                    self.children[i].append(Circle(radius, x, y))

            #子の円の削減
            if random.randint(0,100)<self.MUTATION_PROLABILITY:
                print("rm child")
                if len(self.children[i])>2:
                    self.children[i].pop()

    #点数付け
    def grading(self, heredity_index):
        circles = self.children[heredity_index]
        eva = Evaluation.Evaluation.Evaluation()
        score = eva.evaluate(circles, self.picture_data)
        self.scores[heredity_index] = score

    #親を見つける
    #一番目に強い親と2番めに強い親を持ってくる
    def findParent(self):
        #index score
        no1 = [-1, -1]
        no2 = [-1, -1]
        for i in range(self.HEREDITY_NUM):
            if self.scores[i] > no1[1]:
                no2[0] = no1[0]
                no2[1] = no1[1]
                no1[1] = self.scores[i]
                no1[0] = i
            elif self.scores[i]>no2[1]:
                no2[1] = self.scores[i]
                no2[0] = i

        parents = []
        parents.append(no1[0])
        parents.append(no2[0])
        return parents

import Evaluation.PictureData
picture_data = Evaluation.PictureData.PictureData()
picture_data.width = 1000
picture_data.height = 1000

h = Heredity(picture_data)
h.getExcellent()
for child in h.children:
    for circle in child:
        print(circle.radius)