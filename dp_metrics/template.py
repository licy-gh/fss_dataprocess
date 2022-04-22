'''
目前调用了pandas和numpy依赖包，可以使用其中的所有方法，有需要可以自行调用额外的包
辅助实现，如果调用的别的包记得把依赖打包添加到华为云FunctionGraph的依赖包中
'''
import pandas as pd
import numpy as np

'''
注释标一下函数的功能
'''
def template(data): # def 函数的名字要和文件名一致
    '''输入数据采用json格式
    {
        "operation": "...",
        "parameters": [..., ...],
        "src1": [..., ...],
        "src2": [..., ...]
    }
    '''
    src = pd.DataFrame(data['src']) # 只有单个输入，取操作数
    src1 = pd.DataFrame(data['src1']) # 有多个输入时，取操作数1
    src2 = pd.DataFrame(data['src2']) # 有多个输入时，取操作数2，以此类推

    parameters = pd.DataFrame(data['parameters']) # 用户输入的参数，以list传入

    res = []
    # 实现函数逻辑进行操作，结果输出到res中

    return res # 函数返回类型为list