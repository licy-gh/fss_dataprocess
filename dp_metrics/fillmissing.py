import pandas as pd
import numpy as np

'''
F = fillmissing(A,'constant',v) 使用常量值 v 填充缺失的数组或表条目。如果 A 是矩阵或多维数组，则 v 可以是标量或向量。
如果 v 是向量，每个元素指定 A 对应列中的填充值。如果 A 是表或时间表，则 v 也可以是元胞数组，其元素包含每个表变量的填充值。
缺失值的定义取决于 A 的数据类型：
NaN - double、single、duration 和 calendarDuration
NaT — datetime
<missing> — string
<undefined> — categorical
' ' — char
{''} - 字符数组的 cell
如果 A 是表，则每列的数据类型定义该列的缺失值。
'''
def fillmissing(data):
    src = pd.DataFrame(data['src'])
    return src.fillna(method='pad').values.tolist()