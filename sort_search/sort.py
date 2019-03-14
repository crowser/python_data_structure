#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def swop(swop_obj, index1, index2):
    swop_obj[index1], swop_obj[index2] = swop_obj[index2], swop_obj[index1]


def bubbing(alist):
    """冒泡排序"""
    alist_len = len(alist)
    for x in range(alist_len-1):
        for y in range(x+1, alist_len):
            if alist[x] > alist[y]:
                swop(alist, x, y)


def select(alist):
    """选择排序"""
    alist_len = len(alist)
    for x in range(alist_len-1):
        min_index = x
        for y in range(x+1, alist_len):
            if alist[min_index] > alist[y]:
                min_index = y
        swop(alist, x, min_index)


def insert(alist):
    """插入排序"""
    alist_len = len(alist)
    for x in range(1, alist_len):
        for y in range(x):
            if alist[y] > alist[x]:
                temp = alist[x]
                for z in reversed(range(y, x)):
                    alist[z+1] = alist[z]
                alist[y] = temp


list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert(list1)
print(list1)




