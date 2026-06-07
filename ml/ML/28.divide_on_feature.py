# 描述
# 实现一个函数来根据特定特征的阈值将数据集分成两个子集。这是决策树算法中的一个基本操作，用于根据特征值对数据进行二分划分。

# 划分规则：
# - 对于数值型阈值：将特征值大于等于阈值的样本划分到第一个子集，小于阈值的样本划分到第二个子集
# - 对于非数值型阈值：将特征值等于阈值的样本划分到第一个子集，不等于阈值的样本划分到第二个子集

# 输入描述：
# 函数`divide_on_feature`接收三个参数：
# 1. X：数据集，二维numpy数组
# 2. feature_i：用于划分的特征索引，整数
# 3. threshold：划分阈值，可以是数值或其他类型

# 输出描述：
# 返回一个包含两个numpy数组的列表：
# 1. 第一个数组包含满足条件的样本
# 2. 第二个数组包含不满足条件的样本


# 输入：
# [[1, 2], [3, 4], [5, 6]]
# 0
# 3

# 输出：
# [array([[3, 4],
#        [5, 6]]), array([[1, 2]])]

import numpy as np

def divide_on_feature(X, feature_i, threshold):
    divide_func = None
    if isinstance(threshold, int) or isinstance(threshold, float):
        divide_func = lambda sample : sample[feature_i] >= threshold
    else:
        divide_func = lambda sample : sample[feature_i] == threshold
    X1 = [sample for sample in X if divide_func(sample)]
    X2 = [sample for sample in X if not divide_func(sample)]
    
    return [np.array(X1), np.array(X2)]

    
if __name__ == "__main__":
    X = np.array(eval(input()))
    feature_i = int(input())
    threshold = eval(input())
    print(divide_on_feature(X, feature_i, threshold))

