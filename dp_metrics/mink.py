import pandas as pd
import numpy as np

'''
B = mink(A,k) 返回 A 的 k 个最小元素。
如果 A 是向量，则 mink 返回一个向量，其中包含 A 的 k 个最小元素。
如果 A 是矩阵，则 mink 返回一个矩阵，该矩阵的列包含 A 的每一列中的 k 个最小元素。
如果 A 是多维数组，则 mink 返回大小不等于 1 的第一个维度上的 k 个最小元素。
'''
def mink(data):
    src = pd.DataFrame(data['src'])
    param = data['parameters'][0]
    res = src.nsmallest(param, columns=0)
    return res[0].values.tolist()