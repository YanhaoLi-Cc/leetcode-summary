# 描述
# 编写一个主成分分析 (PCA) 的 Python 函数。
# 该函数采用一个 2维 NumPy 数组作为输入，其中每行代表一个数据样本，每列代表一个特征。
# 该函数主要做以下功能：标准化数据集，计算协方差矩阵，找到特征值和特征向量，并返回主成分（与最大特征值对应的特征向量）。
# 该函数还应采用整数 k 作为输入，表示要返回的主成分的数量。

# 1. 标准化数据 (Standardization)
# 将输入数据标准化，使得每个特征的均值为 0，方差为 1。其数学表达式为：
# $$x_{standardized} = \frac{x - \mu}{\sigma}$$

# 2. 计算协方差矩阵 (Covariance Matrix)
# 计算标准化后的数据协方差矩阵。其数学表达式为：
# $$covariance\_matrix = \frac{1}{m - 1} \times (X^T \times X)$$

# 3. 计算特征值和特征向量 (Eigenvalues and Eigenvectors)
# 计算协方差矩阵的特征值和特征向量。其数学（代码）表达式为：
# $$eigenvalues, eigenvectors = np.linalg.eig(covariance\_matrix)$$

# 4. 选择主成分 (Principal Components Selection)
# 选择特征值最大的 $k$ 个特征向量作为主成分。其数学（代码）表达式为：
# $$principal\_components = eigenvectors[:, :k]$$

# 输入描述：
#   第1行输入一个2维 NumPy 数组，第2行输入一个整数 k 。
# 输出描述：
#   输出主成分。

# 输入：
# [[1, 4, 7], [3, 6, 9], [2, 5, 8], [4, 7, 10], [5, 8, 11]]
# 1

# 输出：
# [[0.5774]
#  [0.5774]
#  [0.5774]]


import numpy as np

def pca(data, k):
    # 1. 标准化：每个特征减去均值，除以标准差，使均值为0、方差为1
    x_normed = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

    # 2. 计算协方差矩阵：X^T·X / (m-1)，rowvar=False 表示列是特征
    covariance_matrix = np.cov(x_normed, rowvar=False)

    # 3. 特征分解：eig 返回 (特征值数组, 特征向量矩阵)，每列是一个特征向量
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    # 4. 按特征值从大到小排序，同步调整特征向量列顺序
    idx = np.argsort(eigenvalues)[::-1]  # 降序索引
    eigenvalues_sorted = eigenvalues[idx]
    eigenvectors_sorted = eigenvectors[:, idx]

    # 5. 取前 k 列（最大 k 个特征值对应的特征向量）= 主成分
    principal_components = eigenvectors_sorted[:, :k]

    return np.round(principal_components, 4)
    
    

# 主程序
if __name__ == "__main__":
    # 输入数组
    data = input()
    k = input()

    # 处理输入
    import ast
    data = ast.literal_eval(data)
    k = int(k)

    # 调用函数计算
    output = pca(data,k)
    
    # 输出结果
    print(output)