import pandas as pd
import numpy as np

'''
R = rmmissing(A) 从数组或表中删除缺失的条目。如果 A 是向量，则 rmmissing 会删除包含缺失数据的所有条目。如果 A 是矩阵或表，则 rmmissing 会删除包含缺失数据的所有行。缺失值的定义取决于 A 的数据类型：
NaN - double、single、duration 和 calendarDuration
NaT — datetime
<missing> — string
<undefined> — categorical
' ' — char
{''} - 字符数组的 cell
'''
def rmmissing(data):
    src = pd.DataFrame(data['src'])
    return src.dropna().values.tolist()