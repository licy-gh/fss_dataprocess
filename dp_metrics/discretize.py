import pandas as pd
import numpy as np

'''
将数据划分为 bin 或类别
'''
def discretize(data):
    src = pd.DataFrame(data['src1']).values.tolist()
    k = pd.DataFrame(data['src2']).values.tolist()
    return np.digitize(src[0], k[0]).tolist()