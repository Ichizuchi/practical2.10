#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поиск среднего гармонического аргументов
def harmonic_mean(*args):

    if args:
        values = [float(arg) for arg in args]
        product = 0
        for value in values:
            product += 1/value
        return round(len(values)/product, 4)
    else:
        return None


if __name__ == "__main__":
    print(harmonic_mean(1, 2, 6))
    print(harmonic_mean(30, 19, 7))
