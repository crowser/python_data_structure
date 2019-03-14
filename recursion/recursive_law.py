#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def listsum(items):
    if len(items) == 1:
        return items[0]
    else:
        return listsum(items[1:]) + items[0]


def divide_by2(dec_number):
    if dec_number == 1:
        return str(1)
    else:
        return divide_by2(dec_number // 2) + str(dec_number % 2)




