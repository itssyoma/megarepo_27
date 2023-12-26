#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Ввод строки с клавиатуры
    string = input("Введите строку: ")

    # Создание множества гласных
    vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

    # Подсчет количества гласных в строке
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1

    print("Количество гласных в строке:", count)
