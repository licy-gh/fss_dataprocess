import pandas as pd
import numpy as np
'''
M = mean(A) 返回 A 沿大小不等于 1 的第一个数组维度的元素的均值。

如果 A 是向量，则 mean(A) 返回元素均值。

如果 A 为矩阵，那么 mean(A) 返回包含每列均值的行向量。

如果 A 是多维数组，则 mean(A) 沿大小不等于 1 的第一个数组维度计算，并将这些元素视为向量。此维度会变为 1，而所有其他维度的大小保持不变。


'''
def mean(data):
    src = pd.DataFrame(data['src'])
    return src.mean().values.tolist()