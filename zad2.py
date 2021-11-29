#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def garmonic(*args):
    if args:
        values = [int(arg) for arg in args]

        k = len(values)
        i, summ = 0, 0
        for i in values:
            summ += 1 / i
        garmonica = k / summ
        return garmonica
    else:
        return None


if __name__ == "__main__":
    numbers = input('Введите аргументы: ').split()
    print('Среднее гармоническое значение ваших аргументов -- ', garmonic(*numbers))
