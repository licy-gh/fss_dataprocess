import pandas as pd
import numpy as np

'''
C = cov(A) 返回协方差。
如果 A 是由观测值组成的向量，则 C 为标量值方差。
如果 A 是其列表示随机变量或行表示观测值的矩阵，则 C 为对应的列方差沿着对角线排列的协方差矩阵。
C 按观测值数量 -1 实现归一化。如果仅有一个观测值，应按 1 进行归一化。
如果 A 是标量，则 cov(A) 返回 0。如果 A 是空数组，则 cov(A) 返回 NaN。
'''
def cov(data):
    src = pd.DataFrame(data['src'])
    return np.cov(src).tolist()