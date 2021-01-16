#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/16 6:03 PM
# @Author: wisdom
# @File:combinedTwoSortedArray.py

from typing import List


def merge(self, n, m, A, B):
    if not A and not B:
        return []
    elif not A:
        return B
    elif not B:
        return A
    while m > 0 and n > 0:
        if A[m - 1] > B[n - 1]:
            A[m + n - 1] = A[m - 1]
            m -= 1
        else:
            A[m + n - 1] = B[n - 1]
            n -= 1
    if n > 0:
        A[:n] = B[:n]
    return A


if __name__ == '__main__':
    listA = []
    listB = []
    result = []
    n = int(input())
    m = int(input())
    for i in range(0, n):
        num = int(input())
        listA.append(num)
    for i in range(0, m):
        num = int(input())
        listB.append(num)
    result = merge(n, m, listA, listB)
    print(result)
