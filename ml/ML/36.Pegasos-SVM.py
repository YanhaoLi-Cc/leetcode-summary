# 描述
# 实现Pegasos（Primal Estimated sub-GrAdient SOlver for SVM）算法来训练核支持向量机（Kernel SVM）分类器。
# Pegasos是一种高效的随机梯度下降算法，用于解决SVM优化问题。
# 在权重更新时，只需要对不符合约束的样本进行更新，SGD的一次迭代过程需要遍历所有数据。

#  线性核的公式为
# $$K(x,y) = x \cdot y$$
# RBF核公式
# $$K(x,y) = e^{-\frac{||x-y||^2}{2\sigma^2}}$$
# 决策函数公式
# $$f(x_i) = \sum_{j=1}^{n} \alpha_j \cdot y_j \cdot K(x_j, x_i) + b$$
# 模型对样本 x_i 的预测结果为 sign(f(x_i))
#
# 学习率衰减公式
# $$\eta_t = \frac{1}{\lambda \cdot t}$$
# 权重更新公式（仅当 y_i * f(x_i) < 1 时更新）
# $$\alpha_i = \alpha_i + \eta_t * (y_i - \lambda * \alpha_i)$$
# $$b = b + \eta_t * y_i$$

# 其中，lambda 为正则化参数，用于防止过拟合，eta_t为第t轮迭代的学习率，随迭代次数衰减。约束条件 y_i * f(x_i) >= 1 表示样本应正确分类且在间隔之外，不满足时才更新参数。

# 输入描述：
# 函数接收6个参数：
# 1. data：二维numpy数组，每行是一个样本的特征向量
# 2. labels：一维numpy数组，包含对应的二分类标签（-1或1）
# 3. kernel：字符串，指定核函数类型（'linear'或'rbf'）
# 4. lambda_val：浮点数，正则化参数
# 5. iterations：整数，算法迭代次数
# 6. sigma：浮点数，RBF核函数的带宽参数

# 输出描述：
# 返回一个元组，包含两个元素：
# 1. alpha：列表，每个样本对应的alpha系数（保留4位小数）
# 2. bias：浮点数，模型的偏置项（保留4位小数）

# 输入：
# [[1, 2], [2, 3]]
# [1, -1]
# 'linear'
# 0.01
# 100
# 1.0
# 输出：
# ([100.0, -100.0], -418.7378)




import numpy as np

def linear_kernel(x, y):
    return np.dot(x, y)

# $$K(x,y) = e^{-\frac{||x-y||^2}{2\sigma^2}}$$
def rbf_kernel(x, y, sigma):
    return np.exp( - (np.linalg.norm(x - y) ** 2) / (2 * sigma ** 2))

def pegasos_kernel_svm(data, labels, kernel='linear', lambda_val=0.01, iterations=100, sigma=1.0):
    
    data_len = len(data)
    alphas = np.zeros(data_len)
    bias = 0
    
    for iter in range(1, iterations + 1):
        for i in range(data_len):

            if kernel == 'linear':
                kernel_fun = linear_kernel
            elif kernel == 'rbf':
                kernel_fun = lambda x, y : rbf_kernel(x, y, sigma)
                
            # $$f(x_i) = \sum_{j=1}^{n} \alpha_j \cdot y_j \cdot K(x_j, x_i) + b$$
            decision = sum(alphas[j] * labels[j] * kernel_fun(data[j], data[i]) for j in range(data_len)) + bias

            # $$\eta_t = \frac{1}{\lambda \cdot t}$$
            eta_t = 1.0 / (lambda_val * iter)
            
            # y_i * f(x_i) < 1
            if labels[i] * decision < 1:
                # $$\alpha_i = \alpha_i + \eta_t * (y_i - \lambda * \alpha_i)$$
                # $$b = b + \eta_t * y_i$$
                alphas[i] += eta_t * (labels[i] - lambda_val * alphas[i])
                bias += eta_t * labels[i]
                
    return ([round(alpha, 4) for alpha in alphas], round(bias, 4))

if __name__ == "__main__":
    data = np.array(eval(input()))
    labels = np.array(eval(input()))
    kernel = eval(input())
    lambda_val = float(input())
    iterations = int(input())
    sigma = float(input())
    print(pegasos_kernel_svm(data, labels, kernel, lambda_val, iterations, sigma))