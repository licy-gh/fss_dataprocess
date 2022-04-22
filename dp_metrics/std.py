import pandas as pd
import numpy as np
'''
S = std(A) 返回 A 沿大小不等于 1 的第一个数组维度的元素的标准差。

如果 A 是观测值的向量，则标准差为标量。

如果 A 是一个列为随机变量且行为观测值的矩阵，则 S 是一个包含与每列对应的标准差的行向量。

如果 A 是多维数组，则 std(A) 会沿大小不等于 1 的第一个数组维度计算，并将这些元素视为向量。此维度的大小将变为 1，而所有其他维度的大小保持不变。

默认情况下，标准差按 N-1 实现归一化，其中 N 是观测值数量。

'''
def std(data):
    src = pd.DataFrame(data['src'])
    return src.std().values.tolist()