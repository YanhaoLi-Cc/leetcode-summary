# 描述
# 编写一个函数，从头开始执行 k -Fold 交叉验证数据拆分。
# 该函数输入一个数据集（一个 2维 NumPy 数组，其中每行代表一个数据样本，每列代表一个特征）和代表折叠数量的整数 k。
# 该函数应将数据集分成 k 个部分，一个部分作为测试集，其余部分作为训练集，并返回一个列表，其中每个元素都是一个元组，其中包含每次折叠的训练集和测试集。

# 输入描述：
# 第1行输入一个数据集，第2行输入整数k。
# 输出描述：
# 输出一个列表，每个元素都是一个元组，其中包含每次折叠的训练集和测试集。

# 输入：
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
# 3

# 输出：
# [[[[7, 8, 9], [1, 2, 3], [10, 11, 12]], [[4, 5, 6], [13, 14, 15]]], [[[4, 5, 6], [13, 14, 15], [10, 11, 12]], [[7, 8, 9], [1, 2, 3]]], [[[4, 5, 6], [13, 14, 15], [7, 8, 9], [1, 2, 3]], [[10, 11, 12]]]]



import numpy as np


def cross_validation_split(data, k, seed=42):
    np.random.seed(seed)
    np.random.shuffle(data)  # 先打乱，保证每折数据分布均匀

    # 1. 将数据连续切成 k 折，前 extra 折多分一行
    data_len = len(data)
    folds = []
    start = 0
    step = data_len // k       # 每折基础大小
    extra = data_len % k       # 多出的样本数，分给前 extra 折
    for i in range(k):
        new_step = step + 1 if i < extra else step  # 前 extra 折多拿一个
        folds.append(data[start:start + new_step])   # 连续切片
        start += new_step

    # 2. 遍历每折：该折做测试集，其余合并做训练集
    result = []
    for i in range(k):
        train = []
        for j in range(k):
            if j != i:
                train.extend(folds[j])  # 把非测试折的行逐一加入训练
        test = folds[i]
        result.append([np.array(train).tolist(), np.array(test).tolist()])

    return result


# 主程序
if __name__ == "__main__":
    # 输入矩阵和向量
    matrix_inputx = input()
    k = input()

    # 处理输入
    import ast

    matrix = np.array(ast.literal_eval(matrix_inputx))
    k = int(k)

    # 调用函数计算逆矩阵
    output = cross_validation_split(matrix, k)

    # 输出结果
    print(output)
