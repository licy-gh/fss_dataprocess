import pandas as pd
import numpy as np

'''
B = maxk(A,k) 返回 A 的 k 个最大元素。

如果 A 是向量，则 maxk 返回一个向量，其中包含 A 的 k 个最大元素。

如果 A 是矩阵，则 maxk 返回一个矩阵，此矩阵的列中包含 A 的每一列中的 k 个最大元素。

如果 A 是多维数组，则 maxk 返回大小不等于 1 的第一个维度上的 k 个最大元素。


'''
def maxk(data):
    src = pd.DataFrame(data['src'])
    param = data['parameters'][0]
    res = src.nlargest(param, columns=0)
    return res[0].values.tolist()