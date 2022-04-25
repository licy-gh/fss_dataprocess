import pandas as pd
import numpy as np

'''
返回相关系数的矩阵
'''
def corrcoef(data):
    src = pd.DataFrame(data['src'])
    return np.corrcoef(src).tolist()