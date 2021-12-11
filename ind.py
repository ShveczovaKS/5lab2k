#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def summy(*args):
    if args:
        summa = 0
        numma = 0

        values = [float(arg) for arg in args]

        for inx in values:
            if inx < 0:
                numma += 1
            if numma == 1 and inx > 0:
                summa += inx
            if numma == 2:
                print(summa)
    else:
        return None


if __name__ == "__main__":
    print(summy(-1, 100, 0.2, 3, -1))
    print(summy(15, 90, -14, 15, 15, 0.5, -1))
