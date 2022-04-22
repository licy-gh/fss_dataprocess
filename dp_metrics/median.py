import pandas as pd
import numpy as np
'''
M = median(A) 返回 A 的中位数值。

如果 A 为向量，则 median(A) 返回 A 的中位数值。

如果 A 为非空矩阵，则 median(A) 将 A 的各列视为向量，并返回中位数值的行向量。

如果 A 为 0×0 空矩阵，median(A) 返回 NaN。

如果 A 为多维数组，则 median(A) 将沿大小不等于 1 的第一个数组维度的值视为向量。此维度的大小将变为 1，而所有其他维度的大小保持不变。

'''
def median(data):
    src = pd.DataFrame(data['src'])
    return src.median().values.tolist()