# 实现三种不同的梯度下降算法，使用均方误差(MSE)作为损失函数。需要实现以下三种变体：
# 1. 批量梯度下降(Batch Gradient Descent)
# 2. 随机梯度下降(Stochastic Gradient Descent)
# 3. 小批量梯度下降(Mini-batch Gradient Descent)
# $$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

# 输入描述：
# 函数`gradient_descent`接收七个参数：
# 1. X：特征矩阵，形状为(m, n)
# 2. y：目标值向量，形状为(m,)
# 3. weights：初始权重向量，形状为(n,)
# 4. learning_rate：学习率
# 5. n_iterations：迭代次数
# 6. batch_size：批量大小（仅用于mini-batch方法）
# 7. method：使用的方法（'batch', 'stochastic' 或 'mini_batch'）
# 输出描述：
# 返回一个numpy数组，表示最终优化的权重向量。

# 算法通过迭代更新参数来最小化损失函数，具体步骤为：
# MSE 损失函数的梯度公式（ŷ = X @ w）：
#   $$g_t = \nabla MSE = \frac{2}{n} X^T(\hat{y} - y)$$
# 更新参数：$w_{t+1} = w_t - \eta \cdot g_t$

# 三种变体的区别在于每次更新使用的数据量：
# 1. Batch：一次用全部 m 个样本 → 每 epoch 更新 1 次
# 2. Stochastic：一次用 1 个样本 → 每 epoch 更新 m 次（逐个遍历）
# 3. Mini-batch：一次用 batch_size 个样本 → 每 epoch 更新 ceil(m/batch_size) 次（顺序切分）

# 输入：
# [[1, 2], [3, 4], [5, 6]]
# [2, 4, 6]
# [0.5, 0.5]
# 0.01
# 100
# 2
# 'batch'

# 输出：
# [0.46201996 0.63526154]

import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
    m, n = X.shape  # m 样本数, n 特征数

    for _ in range(n_iterations):  # 外层循环 = epoch
        if method == 'batch':
            # 用全部样本计算梯度，更新 1 次
            pred = X @ weights
            grad = 2 * X.T @ (pred - y) / m
            weights = weights - learning_rate * grad

        elif method == 'stochastic':
            # 逐个样本计算梯度，更新 m 次
            for i in range(m):
                pred = X[i] @ weights             # 单个样本的预测值（标量）
                grad = 2 * X[i] * (pred - y[i])   # 单个样本的梯度向量
                weights = weights - learning_rate * grad

        elif method == 'mini_batch':
            # 按 batch_size 顺序切分，每批更新 1 次
            for start in range(0, m, batch_size):
                X_b = X[start:start + batch_size]  # 当前批次特征
                y_b = y[start:start + batch_size]  # 当前批次标签
                pred = X_b @ weights                # 批次预测值
                grad = 2 * X_b.T @ (pred - y_b) / batch_size
                weights = weights - learning_rate * grad

    return weights


if __name__ == "__main__":
    X = np.array(eval(input()))
    y = np.array(eval(input()))
    weights = np.array(eval(input()))
    learning_rate = eval(input())
    n_iterations = eval(input())
    batch_size = eval(input())
    method = eval(input())
    print(gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size, method))
