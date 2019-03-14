#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basic_data_structure.stack_queue import Stack


class BinaryTree:
    """ 二叉树 """

    def __init__(self, root_obj):
        self._key = root_obj
        self._left_child = None
        self._right_child = None

    def insert_left(self, new_node):
        if self._left_child is None:
            self._left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t._left_child = self._left_child
            self._left_child = t

    def insert_right(self, new_node):
        if self._right_child is None:
            self._right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t._right_child = self._right_child
            self._right_child = t

    def get_left_child(self):
        return self._left_child

    def get_right_child(self):
        return self._right_child

    def set_root_value(self, obj):
        self._key = obj

    def get_root_value(self):
        return self._key

    def preorder(self):
        """ 前序遍历 """
        yield self.get_root_value()
        if self.get_left_child():
            yield from self.get_left_child().preorder()
        if self._right_child:
            yield from self.get_right_child().preorder()

    def order(self):
        stack = Stack()
        node = self
        while (not stack.is_empty()) or node:
            while node:
                yield node.get_root_value()
                stack.push(node)
                node = node.get_left_child()
            node = stack.pop()
            node = node.get_right_child()


def preorder(tree):
    if tree:
        yield tree.get_root_value()
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


if __name__ == '__main__':
    b = BinaryTree(1)
    b.insert_left(2)
    b.insert_right(3)
    b.get_left_child().insert_left(4)
    b.get_right_child().insert_right(5)
    b.get_left_child().get_left_child().insert_right(6)
    b.get_left_child().get_left_child().get_right_child().insert_left(7)
    b.get_left_child().get_left_child().get_right_child().insert_right(8)

    print(list(b.preorder()))
    print()
    print(list(b.order()))
