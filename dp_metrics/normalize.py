import pandas as pd
import numpy as np

'''
N = normalize(A) 按向量返回 A 中数据的 z 值（中心为 0、标准差为 1）。
如果 A 是向量，则 normalize 对整个向量进行运算。
如果 A 是矩阵、表或时间表，则 normalize 分别对数据的每个列进行运算。
如果 A 为多维数组，则 normalize 沿大小不等于 1 的第一个数组维度进行运算。
'''
def normalize(data):
    src = pd.DataFrame(data['src'])
    return (src/np.linalg.norm(src)).values.tolist()