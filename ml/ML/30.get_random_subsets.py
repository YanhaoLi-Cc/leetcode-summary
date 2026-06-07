# 描述
# 实现一个函数来生成数据集的随机子集。这在机器学习中常用于数据采样、交叉验证和集成学习等场景。函数需要支持有放回和无放回两种采样方式。
# 输入描述：
# 函数`get_random_subsets`接收四个参数：
# 1. X：特征矩阵，二维numpy数组，形状为(n_samples, n_features)
# 2. y：标签向量，一维numpy数组，形状为(n_samples,)
# 3. n_subsets：需要生成的子集数量，整数
# 4. replacements：是否允许重复采样，布尔值，默认为True

# 输出描述：
# 返回一个列表，包含n_subsets个元组：
# - 每个元组包含(X_subset, y_subset)
# - X_subset是特征子集
# - y_subset是对应的标签子集
# - 所有数组都转换为Python列表

# 输入：
# [[1, 2], [3, 4], [5, 6]]
# [0, 1, 0]
# 2

# 输出：
# [([[5, 6], [1, 2], [5, 6]], [0, 0, 0]), ([[5, 6], [1, 2], [1, 2]], [0, 0, 0])]


import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
    np.random.seed(seed)
    m, n = X.shape  # m 样本数, n 特征数

    # 确定每次抽多少：有放回抽全量（bootstrap），无放回抽一半（生成差异子集）
    choice_size = m if replacements else m // 2

    # 生成 n_subsets 组随机行索引，每组长度 choice_size
    indexs = [np.random.choice(m, choice_size, replace=replacements) for _ in range(n_subsets)]

    # 按索引取出对应的 X 和 y
    result = []
    for idx in indexs:
        result.append((X[idx].tolist(), y[idx].tolist()))
    return result
    
if __name__ == "__main__":
    X = np.array(eval(input()))
    y = np.array(eval(input()))
    n_subsets = int(input())
    print(get_random_subsets(X, y, n_subsets))