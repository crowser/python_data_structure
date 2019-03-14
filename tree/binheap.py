#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinHeap:
    def __init__(self):
        self.__heap_list = [0]
        self.__current_size = 0

    def printbinheap(self):
        print(self.__heap_list[1:])

    def insert(self, k):
        self.__heap_list.append(k)
        self.__current_size += 1
        self.__perc_up(self.__current_size)

    def del_min(self):
        retval = self.__heap_list[1]
        self.__heap_list[1] = self.__heap_list.pop()
        self.__current_size -= 1
        self.__perc_down(1)
        return retval

    def build_heap(self, alist):
        i = len(alist) // 2
        self.__current_size = len(alist)
        self.__heap_list = [0] + alist[:]
        while i>0:
            self.__perc_down(i)
            i = i - 1

    def __perc_up(self, i):
        while i//2 > 0:
            if self.__heap_list[i] < self.__heap_list[i//2]:
                self.__heap_list[i], self.__heap_list[i//2] = self.__heap_list[i//2], self.__heap_list[i]
            i = i//2

    def __perc_down(self, i):
        while (i*2) <= self.__current_size:
            mc = self.__min_child(i)
            if self.__heap_list[i] > self.__heap_list[mc]:
                self.__heap_list[i], self.__heap_list[mc] = self.__heap_list[mc], self.__heap_list[i]
            i = mc

    def __min_child(self, i):
        if i * 2 +1 > self.__current_size:
            return i * 2
        elif self.__heap_list[i*2] < self.__heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

b = BinHeap()
alist = [4, 5, 6, 2, 3]
b.build_heap(alist)
b.printbinheap()





