# 实现使用梯度下降法求解Lasso回归（L1正则化线性回归）。
# Lasso回归通过在损失函数中添加L1正则化项来实现特征选择和防止过拟合。
# 梯度下降方式使用批量梯度下降。

# 目标函数 $$J(w, b) = \frac{1}{2n} \sum (y_i - (\sum X_{ij} w_j + b))^2 + \alpha \sum |w_j|$$
# 参数详细说明该公式由均方误差（MSE）项和 L1 正则化项组成，具体参数含义如下：
# $n$：样本数量。
# $y_i$：第 $i$ 个样本的真实值。
# $X_{ij}$：第 $i$ 个样本的第 $j$ 个特征值。
# $w_j$：第 $j$ 个特征的权重。
# $b$：偏置项（Bias）。
# $\alpha$：正则化参数（也称为惩罚系数，用于控制模型的复杂度以防止过拟合）。

# 输入描述：
# 函数`l1_regularization_gradient_descent`接收五个参数：
# 1. X：特征矩阵，形状为(n_samples, n_features)
# 2. y：目标值向量
# 3. alpha：正则化参数，默认0.1
# 4. learning_rate：学习率，默认0.01
# 5. max_iter：最大迭代次数，默认1000
# 6. tol：收敛阈值，默认1e-4

# 输出描述：
# 返回一个元组，包含：
# 1. weights：特征权重向量
# 2. bias：偏置项
# 结果保留3位小数

# 输入：
# [[1, 2], [2, 4], [3, 5]]
# [2, 4, 5]
# 0.1
# 输出：
# [0.061, 0.889] 0.284

import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
    m, n = X.shape
    weights = np.zeros(n, dtype=float)  # w 初始化为 0
    bias = 0                             # b 初始化为 0

    for _ in range(max_iter):
        pred = X @ weights + bias        # ŷ = Xw + b
        error = pred - y                 # ŷ - y

        # 梯度推导：
        # J = 1/(2n)Σ(y-ŷ)² + αΣ|w|
        # ∇_w = (1/n)Xᵀ(ŷ-y) + α·sign(w)  ← 1/2 与平方求导的 2 抵消
        # ∇_b = (1/n)Σ(ŷ-y)              ← 偏置不参与 L1 正则化
        grad_w = X.T @ error / m + alpha * np.sign(weights)
        grad_b = np.sum(error / m)

        weights = weights - learning_rate * grad_w
        bias = bias - learning_rate * grad_b

        # 当梯度 L1 范数小于阈值时认为收敛
        if np.linalg.norm(grad_w, ord=1) < tol:
            break

    return [round(w, 3) for w in weights], round(bias, 3)


if __name__ == "__main__":
    X = np.array(eval(input()))
    y = np.array(eval(input()))
    alpha = float(input())
    weights, bias = l1_regularization_gradient_descent(X, y, alpha)
    print(weights, bias)
