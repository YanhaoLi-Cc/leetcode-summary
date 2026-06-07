# 描述
# 实现一个函数来生成数据集的多项式特征。多项式特征是一种特征工程方法，通过组合原始特征的不同次幂来创建新的特征，可以帮助捕捉非线性关系。

# 例如，对于特征[a, b]，degree=2时生成的多项式特征为 
# $$[1, a, b, a^2, ab, b^2]$$

# 输入描述：
# 第一行输入一个二维numpy数组，表示特征矩阵X。
# 第二行输入一个正整数，表示多项式的最高次数degree。

# 输出描述：
# 输出一个二维numpy数组，形状为(n_samples, n_output_features)，其中n_output_features是所有可能的多项式特征组合数。

# 输入：
# [[1, 2], [3, 4]]
# 2

# 输出：
# [[ 1.  1.  2.  1.  2.  4.]
#  [ 1.  3.  4.  9. 12. 16.]]

import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    n_samples, n_features = X.shape

    # 收集 0 到 degree 的所有特征索引组合
    combs = []
    for d in range(degree + 1):
        combs.extend(combinations_with_replacement(range(n_features), d))
    # combs = [(), (0,), (1,), (0, 0), (0, 1), (1, 1)]
    
    # 逐行计算多项式特征值
    X_new = []
    for i in range(n_samples):
        X_row = X[i]
        row = []
        for comb in combs:
            x = 1
            for idx in comb:      # comb=()     → 不循环，x 保持 1
                x *= X_row[idx]    # comb=(0,1)  → x = X_row[0] * X_row[1]
            row.append(x)
        X_new.append(row)

    return np.array(X_new, dtype=float)

if __name__ == "__main__":
    X = np.array(eval(input()))
    degree = int(input())
    print(polynomial_features(X, degree))


