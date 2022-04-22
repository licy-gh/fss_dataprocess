import pandas as pd
import numpy as np

'''
返回数组的最大元素
如果 src 是向量，则 min(src) 返回 src 的最大值。
如果 src 为矩阵，则 min(src) 是包含每一列的最大值的行向量。
如果 src 是多维数组，则 min(src) 沿大小不等于 1 的第一个数组维度计算，并将这些元素视为向量。此维度的大小将变为 1，而所有其他维度的大小保持不变。如果 src 是第一个维度为 0 的空数组，则 min(src) 返回与 src 大小相同的空数组。
'''
def max(data):
    src = pd.DataFrame(data['src'])
    return src.max().values.tolist()