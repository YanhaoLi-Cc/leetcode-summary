# 编写一个实现 k-Means 聚类算法的 Python 函数。
# 该函数应该接受输入并生成最终质心的列表。 k-Means 聚类是一种用于将n点划分为k簇的方法，目标是将相似的点分组在一起，并用其"中心"（称为质心）表示每个组。
# 输入描述：
# 函数输入4个参数
# points ：点列表，其中每个点都是一个坐标元组
# k ：表示要形成的簇数的整数
# initial_centroids ：初始质心点列表，每个点都是一个坐标元组
# max_iterations ：表示要执行的最大迭代次数的整数

# 1. 随机选择 k 个点作为初始聚类中心。
# 2. 将每个点分配到最近的聚类中心 本题使用欧几里得距离作为距离度量，即
# $$d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$
# 3. 更新聚类中心为每个簇的平均值。
# 4. 重复步骤2和步骤3，直到聚类中心不再变化或达到最大迭代次数。

# 输出描述：
# 函数返回：簇的最终质心的列表，其中每个质心都四舍五入，保留小数点后四位，用元组表示。

# 输入：
# [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
# 2
# [(1, 1), (10, 1)]
# 10

# 输出：
# [(1.0, 2.0), (10.0, 2.0)]


import numpy as np

def cal_distance(points, centroid):
    """计算所有点到单个质心的欧氏距离 d = √Σ(x_i - y_i)²，返回长度为 m 的一维数组"""
    # points  (m, d)  所有点
    # centroid  (d,)  单个质心
    # 相减 (m,d) - (d,) → (m,d)  广播减
    # ** 2         → (m,d)  每个坐标差值平方
    # .sum(axis=1) → (m,)   沿特征方向求和
    # np.sqrt()   → (m,)   开方得欧氏距离
    return np.sqrt(((points - centroid) ** 2).sum(axis=1))

def k_means_clustering(points, k, initial_centroids, max_iterations):
    points = np.array(points)                            # (m, d)
    centroids = np.array(initial_centroids, dtype=float) # (k, d)

    for _ in range(max_iterations):
        # 1. 分配：计算 (k, m) 距离矩阵，每行是一个质心到所有点的距离
        distance = [cal_distance(points, c) for c in centroids]
        # 沿 axis=0（行方向）对每列取 argmin，即每个点归属最近质心的编号
        idx = np.argmin(distance, axis=0)  # (m,)  每个点的簇标签

        # 2. 更新：每个簇取所有归属点的均值作为新质心
        new_centroid = np.zeros_like(centroids)  # (k, d)  预占位
        for i in range(k):
            # 筛出第 i 簇的所有点
            point_near = points[i == idx]  # idx == i 更符合语义，但广播下等价
            # 均值更新；若该簇为空（无点归属），保持旧质心
            new_centroid[i] = np.mean(point_near, axis=0) if len(point_near) > 0 else centroids[i]

        # 3. 收敛判断：质心与上一轮完全一致则停止
        if np.all(new_centroid == centroids):
            break
        centroids = new_centroid

    # 结果保留四位小数，转为元组列表
    centroids = np.round(centroids, 4)
    return [(round(i, 4), round(j, 4)) for i, j in centroids]

def main():
    points = eval(input())
    k = int(input())
    initial_centroids = eval(input())
    max_iterations = int(input())
    final_centroids = k_means_clustering(points, k, initial_centroids, max_iterations)
    print(final_centroids)

if __name__ == "__main__":
    main()
