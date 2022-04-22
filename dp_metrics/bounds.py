import pandas as pd
import numpy as np
'''
同时计算向量的最小值和最大值
'''
def bounds(data):
    src = pd.DataFrame(data['src'])
    res = []
    res.append(int(src[0].values.min()))
    res.append(int(src[0].values.max()))
    return res