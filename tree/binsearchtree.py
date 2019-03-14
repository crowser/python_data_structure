#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinarySearchTree:
    def __init__(self, value):
        self.__root = None
        self.__size = 0

    def lenth(self):
        return self.__size

    def __len__(self):
        return self.__size

    def __iter__(self):
        return self.__root.__iter__()

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def hasleftchild(self):
        return self.leftchild

    def hasrightchild(self):
        return self.rightchild

    def isleftchild(self):
        return self.parent and self.parent.leftchild == self

    def isrightchild(self):
        return self.parent and self.parent.rightchild == self

    def isRoot(self):
        return not self.parent

    def isleaf(self):
        return not self.leftchild and not self.rightchild