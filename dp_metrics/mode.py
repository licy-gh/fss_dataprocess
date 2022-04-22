import pandas as pd
import numpy as np
'''
M = mode(A) 返回 A 的样本众数，即 A 中出现次数最多的值。如果有多个值以相同的次数出现，mode 将返回其中最小的值。对复杂的输入，最小值是排序列表的第一个值。

如果 A 为向量，则 mode(A) 返回 A 中出现次数最多的值。

如果 A 为非空矩阵，那么 mode(A) 将返回包含 A 每列众数的行向量。

如果 A 为 0×0 空矩阵，mode(A) 返回 NaN。

如果 A 为多维数组，则 mode(A) 将沿大小不等于 1 的第一个数组维度的值视为向量，并返回一个由出现次数最多的值组成的数组。此维度的大小将变为 1，而所有其他维度的大小保持不变。


'''
def mode(data):
    src = pd.DataFrame(data['src'])
    return src.mode().values.tolist()