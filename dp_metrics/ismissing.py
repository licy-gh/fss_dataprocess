import pandas as pd
import numpy as np

'''
TF = ismissing(A) 返回逻辑数组，指示数组或表中的哪些元素包含缺失值。TF 的大小与 A 的大小相同。
标准缺失值取决于数据类型：
double、single、duration 和 calendarDuration 的指示符为 NaN
datetime 的指示符为 NaT
string 的指示符为 <missing>
categorical 的指示符为 <undefined>
char 的指示符为 ' '
字符向量 cell 的指示符为 {''}
'''
def ismissing(data):
    src = pd.DataFrame(data['src'])
    return src.isnull().values.tolist()