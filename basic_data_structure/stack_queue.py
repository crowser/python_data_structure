#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Stack:
    """A stack encapsulation based on list.

    method: push clear pop peek isEmpty size"""
    def __init__(self):
        self.__items = []

    def push(self, new_item):
        self.__items.append(new_item)

    def clear(self):
        del self.__items[:]

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def is_empty(self):
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)

    def __iter__(self):
        return iter(self.__items[::-1])

    def __next__(self):
        return self.pop()


class Queue:

    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    def isEmpty(self):
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)

    def __iter__(self):
        return iter(self.__items)

    def __next__(self):
        return self.dequeue()


class Deque:

    def __init__(self):
        self.__items = []

    def add_front(self, item):
        self.__items.insert(0, item)

    def add_rear(self, item):
        self.__items.append(item)

    def remove_front(self):
        self.__items.pop(0)

    def remove_rear(self):
        self.__items.pop()

    def is_empty(self):
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)

    def front_iter(self):
        return iter(self.__items)

    def rear_iter(self):
        return iter(self.__items[::-1])
