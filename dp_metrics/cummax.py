import pandas as pd
import numpy as np

'''
M = cummax(A) 返回 A 的累积最大元素。默认情况下，cummax(A) 沿其大小不为 1 的第一个数组维度运算。
如果 A 为向量，则 cummax(A) 返回一个包含 A 的累积最大值的等大小向量。
如果 A 是矩阵，则 cummax(A) 返回一个等大小的矩阵，其中包含 A 的各列中的累积最大值。
如果 A 是多维数组，则 cummax(A) 沿 A 的大小不为 1 的第一个数组维度返回一个等大小的数组，其中包含累积最大值。
'''
def cummax(data):
    src = pd.DataFrame(data['src'])
    return src.cummax().values.tolist()