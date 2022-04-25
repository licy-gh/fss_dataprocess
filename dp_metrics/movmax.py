import pandas as pd
import numpy as np

'''
M = movmax(A,k) 返回由局部 k 个数据点范围内的最大值组成的数组，其中每个最大值基于 A 的相邻元素的长度为 k 的滑动窗计算得出。
当 k 为奇数时，窗口以当前位置的元素为中心。当 k 为偶数时，窗口以当前元素及其前一个元素为中心。
当没有足够的元素填满窗口时，窗口将自动在端点处截断。当窗口被截断时，只根据窗口内的元素计算最大值。M 与 A 的大小相同。
'''
def movmax(data):
    src = pd.DataFrame(data['src1']).values.tolist()
    k = pd.DataFrame(data['src2']).values.tolist()[0][0]
    res=[]
    for i in range(0,len(src)):
        tmp=-1000000
        for j in range(max(0,i-k//2) , min(len(src),i+k//2+1)):
            tmp=max(tmp,src[j][0])
        res.append(tmp)
    return res