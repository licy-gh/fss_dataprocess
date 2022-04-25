import pandas as pd
import numpy as np

'''
TF = isoutlier(A) 返回一个逻辑数组，当在 A 的元素中检测到离群值时，该数组中与之对应的元素为 true。默认情况下，离群值是指与中位数相差超过三倍经过换算的中位数绝对偏差 (MAD) 的值。如果 A 是矩阵或表，则 isoutlier 分别对每一列进行运算。如果 A 是多维数组，则 isoutlier 沿大小不等于 1 的第一个维度进行运算。
'''
def isoutlier(data):
    src = pd.DataFrame(data['src']).values.tolist()
    std = np.std(src,ddof=1)
    mean = np.mean(src)
    cutoff = std * 3
    low = mean - cutoff
    up = mean + cutoff
    res = []
    for i in src:
        if i[0] > up or i[0] < low:
            res.append(i[0])
    return res