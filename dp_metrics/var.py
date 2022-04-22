import pandas as pd
import numpy as np
'''
V = var(A) 返回 A 中沿大小不等于 1 的第一个数组维度的元素的方差。

如果 A 是一个观测值向量，则方差为标量。

如果 A 是一个其各列为随机变量、其各行为观测值的矩阵，则 V 是一个包含对应于每列的方差的行向量。

如果 A 是一个多维数组，则 var(A) 会将沿大小不等于 1 的第一个数组维度的值视为向量。此维度的大小将变为 1，而所有其他维度的大小保持不变。

默认情况下，方差按观测值数量 -1 实现归一化。

如果 A 是标量，则 var(A) 返回 0。如果 A 是一个 0×0 的空数组，则 var(A) 将返回 NaN。

'''
def var(data):
    src = pd.DataFrame(data['src'])
    return src.var().values.tolist()