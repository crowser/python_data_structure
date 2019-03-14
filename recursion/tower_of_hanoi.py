#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from basic_data_structure.stack_queue import Stack


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)


def moveDisk(fromPole, toPole):
    toPole.push(fromPole.pop())


if __name__ == '__main__':
    fromPole = Stack()
    withPole = Stack()
    toPole = Stack()

    for i in range(10, 0, -1):
        fromPole.push(i)

    moveTower(fromPole.size, fromPole, toPole, withPole)

    for i in toPole:
        print(i)
