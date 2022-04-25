import pandas as pd
import numpy as np

'''
返回按排序顺序的前若干行
返回按降序（对于数值数据）或字母顺序倒序（对于文本数据）排序的数组 X 的前 k 行。
'''
def topkrows(data):
    src = pd.DataFrame(data['src'])
    parameters = pd.DataFrame(data['parameters']).iloc[0, 0]
    res = src.sort_values(by=0,ascending=False).head(parameters).values.tolist()
    return res