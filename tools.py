#!/usr/bin/env python
# coding=utf-8
"""
Filename:       validate_code.py
Last modified:  2015-10-14 15:36

Description:

"""

import setting
import os
from PIL import Image


def generate_code():
    i = 0
    for dirpath, dirnames, filenames in os.walk(setting.PIC_DIR):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print file_path
            make_lib(i, file_path)
            i = i + 1


def make_lib(i, file_path):
    img = Image.open(file_path)
    gray_img = img.convert('1')
    gray_img.save('gray.jpg')

    width, height = gray_img.size

    # find each number
    w = 0
    while w < width:
        column = []
        for h in range(height):
            column.append(gray_img.getpixel((w, h)))

        # begining of a number
        if sum(column) / height < 245:
            box = (w, 0, w + 10, 10)
            region = gray_img.crop(box)
            save_path = os.path.join(setting.IMG_DIR, '%s_%s.jpg' % (i, w))
            print 'save_path', save_path
            region.save(save_path)
            w = w + 10
        else:
            w = w + 1


def test():
    generate_code()


if __name__ == "__main__":
    test()
