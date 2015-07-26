# coding: utf-8


class PictureData:
    #picture data
    #0: 出したい部分
    #1: 隠したい部分

    def __init__(self):
        self.picture = [[]]
        self.width = 0
        self.height = 0

    def getPixel(self, x, y):
        if self.width>=x or self.width<0:
            return -1
        elif self.height>=y or self.height<0:
            return -1

        return self.picture[y][x]

    def mustExposed(self, x, y):
        if self.isOutOfRange(x, y):
            return True

        if self.picture[y][x]==0:
            return True
        else:
            return False

    def isOutOfRange(self, x, y):
        if self.width>=x or self.width<0:
            return True
        elif self.height>=y or self.height<0:
            return True

        return False