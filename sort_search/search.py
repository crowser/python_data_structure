#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def binarySearch(alist, item):
    alist.sort()
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if item == alist[midpoint]:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            elif item > alist[midpoint]:
                first = midpoint + 1
    return found


def binarySearch_recursion(alist, item):
    if 0 == len(alist):
        return False
    else:
        midpoint = len(alist) // 2
        if item == alist[midpoint]:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch_recursion(alist[:midpoint], item)
            elif item > alist[midpoint]:
                return binarySearch_recursion(alist[midpoint+1:], item)


l = list(range(99999))
print(binarySearch_recursion(l, 8888))





