#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    # Ввод двух строк с клавиатуры
    string1 = input("Введите первую строку: ")
    if not(string1):
        print("Введенная строка является пустой", file=sys.stderr)
        exit(1)
    string2 = input("Введите вторую строку: ")
    if not(string2):
        print("Введенная строка является пустой", file=sys.stderr)
        exit(1)

    # Создание множеств символов из каждой строки
    set1 = set(string1)
    set2 = set(string2)

    # Нахождение общих символов
    common_chars = set1.intersection(set2)

    if common_chars:
        print("Общие символы в двух строках:", common_chars)
    else:
        print("Общих символов не обнаружено")
