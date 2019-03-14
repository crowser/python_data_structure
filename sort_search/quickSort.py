#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark +1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        if leftmark > rightmark:
            done = True
        else:
            swop(alist, leftmark, rightmark)
    swop(alist, first, rightmark)
    return rightmark

def swop(alist, lindex, rindex):
    alist[lindex], alist[rindex] = alist[rindex], alist[lindex]

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)