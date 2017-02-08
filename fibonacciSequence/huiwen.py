#!/usr/bin/env python
# -*- coding: utf-8 -*-
def huiwen():
    x = int(raw_input("input a number:\n"))
    x = str(x)
    for i in range(len(x)/2):
        if x[i] != x[-i-1]:
            print 'this number is not a huiwen'
            break
    print 'this number is a huiwen'

huiwen()