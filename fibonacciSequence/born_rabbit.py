#!/usr/bin/env python
#coding:utf-8
import sys

def born_rabbit(x):
    if  x <=2 :
        return 1
    else:
        return born_rabbit(x-1)+born_rabbit(x-2)
while 1:
    x = raw_input("months:\n")
    if x == 'q':
        break
    print born_rabbit(int(x))
