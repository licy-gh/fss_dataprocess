import pandas as pd
import numpy as np

'''
M = cummin(A) 返回 A 的累积最小元素。默认情况下，cummin(A) 沿其大小不为 1 的第一个数组维度运算。
如果 A 为向量，则 cummin(A) 返回一个包含 A 的累积最小值的等大小向量。
如果 A 是矩阵，则 cummin(A) 返回一个等大小的矩阵，其中包含 A 的各列中的累积最小值。
如果 A 是多维数组，则 cummin(A) 沿 A 的大小不为 1 的第一个数组维度返回一个等大小的数组，其中包含累积最小值。
'''
def cummin(data):
    src = pd.DataFrame(data['src'])
    return src.cummin().values.tolist()