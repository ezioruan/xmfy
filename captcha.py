#!/usr/bin/env python
# coding=utf-8
"""
Filename:       captcha.py
Last modified:  2015-10-16 16:46

Description:

"""
# coding: utf-8
# captcha.py

import os
from PIL import Image
import setting
from StringIO import StringIO


class Captcha(object):

    def __init__(self):
        self.imglib = {}
        self._loadlib()

    def _loadlib(self):
        """Load characteristic image lib"""

        if not os.path.exists(setting.IMG_DIR):
            print 'Can not find imglib dir.'
            return

        for i in range(10):
            self.imglib[i] = []
            filepath = os.path.join(setting.IMG_DIR, '%d.jpg' % i)
            img = Image.open(filepath).convert('1')
            width, height = img.size
            for w in range(width):
                # store all pixels in a column
                column = []
                for h in range(height):
                    column.append(img.getpixel((w, h)))
                self.imglib[i].append(column)

    def _cmpmatrix(self, listA, listB):
        """Return the count of difference between two list"""

        if len(listA) != len(listB):
            return

        num = 0
        for i, column in enumerate(listA):
            if len(column) != len(listB[i]):
                return
            for j, pixel in enumerate(column):
                if pixel != listB[i][j]:
                    num += 1
        return num

    def _whichnum(self, piexls_matrix):
        """Identify single number"""

        minnum = None
        index = 0
        for i in range(10):
            ret = self._cmpmatrix(self.imglib.get(i, []), piexls_matrix)
            if ret != None:
                if minnum == None or minnum > ret:
                    minnum = ret
                    index = i

        if minnum != None:
            return str(index)
        else:
            return '?'

    def identify(self, image):
        """Identify captcha"""

        img = image.convert('1')

        width, height = img.size

        w = 0
        number = ''
        while w < width:
            column = []
            for h in range(height):
                column.append(img.getpixel((w, h)))

            # begining of a number
            if sum(column) / height < 245:
                piexls_matrix = []
                for i in range(10):
                    piexls_column = []
                    for j in range(10):
                        piexls_column.append(img.getpixel((w + i, j)))
                    piexls_matrix.append(piexls_column)

                number += self._whichnum(piexls_matrix)
                w = w + 10
            else:
                w = w + 1

        return number

if __name__ == '__main__':
    """Test performance of Captcha Class"""
    captcha = Captcha()

    try:
        import requests
        resp = requests.get(setting.VALIDATE_CODE_URL)
        image = Image.open(StringIO(resp.content))
        image.show()
        print captcha.identify(image)
    except Exception, e:
        print 'Download captcha fail.', e
