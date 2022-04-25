在此目录下实现函数.

# 实现描述性统计量(https://ww2.mathworks.cn/help/matlab/descriptive-statistics.html):

## 基本统计量
lcy已实现:min, mink, max, maxk, bounds, mean, median, mode, std, var共10个

后续函数由zrh实现.

在基本统计量中又实现topkrows, corrcoef, cov 共3个
corrcoef,cov目前只处理到传入一个矩阵的情况,两个矩阵视情况可以增加

## 累积统计量
实现 cummax, cummin 共2个

## 移动统计量
实现 movmax, movmin, movmean, movprod, movstd, movvar, movsum, movmedian, movmad 共9个
移动统计量均类似滑动窗口的思想,目前实现处理一维数组,处理长度k作为第二个参数src2传入
movstd和movvar求的是样本标准差和方差

描述性统计量中共实现24个函数

# 数据的预处理(https://ww2.mathworks.cn/help/matlab/referencelist.html?type=function&category=preprocessing-data&s_tid=CRUX_topnav)

## 缺失数据和离群值
实现 ismissing, rmmissing, fillmissing, isoutlier 共4个
fillmissing 采用前一个值填充
isoutlier 将三个标准差范围外的数据点作为异常点加入返回列表
movmad 在之前已实现

## 检测变化点和局部极值
没怎么看懂

## 对数据进行平滑处理和发现趋势
movmean 和 movmedian之前已经实现

## 归一化和缩放数据
实现normalize 1个

## 对数据进行分组和分 bin
实现discretize 1个

