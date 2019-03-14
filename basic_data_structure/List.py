#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:

    def __init__(self, init_data):
        self.__data = init_data
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next


class UnorderedList:

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.__head)
        self.__head = new_node

    def size(self):
        current = self.__head
        number = 0
        while current is not None:
            current = current.get_next()
            number += 1
        return number

    def search(self, item):
        current = self.__head
        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        else:
            return False

    def remove(self, item):
        previous = None
        current = self.__head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.__head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def reversion(self):
        """反转链表"""
        current = self.__head
        previous = None
        next_node = None
        while current is not None:
            if previous is None:
                next_node = current.get_next()
                current.set_next(None)
                previous = current
                current = next_node
            else:
                next_node = current.get_next()
                current.set_next(previous)
                previous = current
                current = next_node
        else:
            self.__head = previous

    def print_list(self):
        current = self.__head
        while current is not None:
            print(current.get_data())
            current = current.get_next()


class OrderedList:

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        current = self.__head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.__head)
            self.__head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current = self.__head
        number = 0
        while current is not None:
            current = current.get_next()
            number += 1
        return number

    def search(self, item):
        current = self.__head
        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        else:
            return False

    def remove(self, item):
        previous = None
        current = self.__head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.__head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def reversion(self):
        """反转链表"""
        current = self.__head
        previous = None
        next_node = None
        while current is not None:
            if previous is None:
                next_node = current.get_next()
                current.set_next(None)
                previous = current
                current = next_node
            else:
                next_node = current.get_next()
                current.set_next(previous)
                previous = current
                current = next_node
        else:
            self.__head = previous

    def print_list(self):
        current = self.__head
        while current is not None:
            print(current.get_data())
            current = current.get_next()
