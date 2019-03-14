#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basic_data_structure.stack_queue import Stack
from basic_data_structure.stack_queue import Queue


def par_checker(symbol_string):
    """括号匹配"""
    s = Stack()
    for symbol in symbol_string:
        if symbol in '([{':
            s.push(symbol)
        elif symbol in ')]}':
            if s.is_empty():
                return False
            else:
                s.pop()
    if s.is_empty():
        return True
    else:
        return False


def divide_by2(dec_number):
    """10进制转2进制"""
    s = Stack()
    while dec_number:
        rem = dec_number % 2
        s.push(int(rem))
        dec_number = (dec_number - rem) / 2
        if dec_number == 1:
            s.push(int(dec_number))
            break
    return ''.join([str(x) for x in s])


def hot_potato(namelist, num):
    """烫手山芋"""
    sim_queue = Queue()
    for name in namelist:
        sim_queue.enqueue(name)
    i = 1
    while sim_queue.size > 1:
        if i == num:
            sim_queue.dequeue()
            i = 1
        else:
            sim_queue.enqueue(sim_queue.dequeue())
            i = i +1

    return sim_queue.dequeue()


if __name__ == "__main__":
    pass








