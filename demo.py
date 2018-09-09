# -*- coding: utf-8 -*-
import math

def findMinAndMax(L):
    if len(L) == 0:
        L_min = None
        L_max = None
    else:
        L_min = min(L)
        L_max = max(L)
    return (L_min,L_max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


