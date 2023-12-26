#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    alphabet = set(chr(i) for i in range(ord('a'), ord('z')))
    A = set('befkt')
    B = set('fijpy')
    C = set('jkly')
    D = set('ijstuyz')

    X = A.intersection(C).union(B.intersection(C))
    Y = A.difference(B).union(D.difference(C))

    print('Множество X: ', X, '\nМножество Y: ', Y)
