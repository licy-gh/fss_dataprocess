# fss_dataprocess
## 1. 代码结构
```
fss_dataprocess
├─dependency/ - 依赖包
├─dp_metrics/ - 实现的数据处理方法
├─.gitattributes - gitattributes配置文件
├─.gitignore - gitignore配置文件
├─index.py - FunctionGraph入口
├─local_test.py - 本地测试文件
└─README.md - 说明文件
```
- `dependency/pandas_numpy.zip`为依赖包，由于华为自带的`pandas`和`numpy`就是一坨屎，所以需要自行导入。本项目所需的所有依赖包都已经打包成一个`pandas_numpy.zip`文件，到时候直接导入即可。如何导入依赖包在之后的“4. 构建函数工作流”一节会说明。
- `dp_metrics/`下实现数据处理的方法，每个方法以**单个**独立`.py`文件形式存放，这样方便管理，整个调度框架我已经全部写完了，你们只需要关注实现接口即可，详见“2. 任务要求”一节。
- `index.py`的`handler`是FunctionGraph的函数入口。

## 2. 任务要求

### 2.1 目标

用python实现 https://ww2.mathworks.cn/help/matlab/descriptive-statistics.html 或者 https://ww2.mathworks.cn/help/matlab/preprocessing-data.html 的函数接口。或者自行实现别的数据处理方面的函数，记得和我说明。

### 2.2 实现

在项目的`dp_metrics/`目录下实现函数，以单个`.py`文件存放，文件名和函数接口保持一致。详细可以参考`dp_metrics/template.py`作为模板。

实例：实现返回数组的最小元素的数据处理函数，函数名称为`min`。

1. 首先在`dp_metrics/`目录下新建`min.py`文件；

2. `min.py`文件中实现`min`函数功能如下：

```python
import pandas as pd
import numpy as np

'''
返回数组的最小元素
如果 src 是向量，则 min(src) 返回 src 的最小值。
如果 src 为矩阵，则 min(src) 是包含每一列的最小值的行向量。
如果 src 是多维数组，则 min(src) 沿大小不等于 1 的第一个数组维度计算，并将这些元素视为向量。此维度的大小将变为 1，而所有其他维度的大小保持不变。如果 src 是第一个维度为 0 的空数组，则 min(src) 返回与 src 大小相同的空数组。
'''
def min(data):
    src = pd.DataFrame(data['src'])
    return src.min().values.tolist()
```

3. 注意def的函数名称要和文件名称保持一致，否则在`index.py`中无法import。

### 2.3 约束

#### 传入的参数

传入的参数只有一项，用户输入的数据data，以json格式存储。只有单个输入时，data的格式为：

```js
{
    "operation": "...", // 用户指定的操作
    "parameters": [..., ...], // 用户对方法传入的参数，没有则为空list
    "src": [..., ...] // 要进行数据处理的对象
}
```

有多个需要输入时，data的格式为：

```js
{
    "operation": "...", // 用户指定的操作
    "parameters": [..., ...], // 用户对方法传入的参数，没有则为空list
    "src1": [..., ...], // 要进行数据处理的对象
    "src2": [..., ...], // 要进行数据处理的对象
    ...
}
```

根据情况自行取值即可。

#### 返回值

返回值类型要求为list。

## 3. 测试

~~TODO。FunctionGraph代码运行逻辑与本地不同，无法直接在本地测试，我什么时候摸一个本地可以测试的代码出来吧。~~

`local_test.py`可以进行简单的本地测试：

1. 建立用户输入的json文件，根据数据格式填写相应字段
2. 在`local_test.py`中第9行修改TEST_PATH参数，对应上面json文件的路径
3. 运行`local_test.py` print输出

输出数据也是json格式：

```js
{
    “res”: [..., ...] // res项对应的就是你们函数的list输出
}
```

本地测试没问题的话，FunctionGraph中也不会出错。

## 4. 构建函数工作流

TODO，摸了。

## 5. Reference

- 函数工作流FunctionGraph文档：https://support.huaweicloud.com/functiongraph/index.html