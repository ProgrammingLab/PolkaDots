# coding: utf-8


class PictureData:

    def __init__(self):
        self.picture = [[]]
        self.width = 0
        self.height = 0

    def getPixel(self, x, y):
        if self.width>=x or self.width<0:
            return 0
        elif self.height>=y or self.height<0:
            return 0

        return self.picture[y][x]