# 实现一个性能指标计算器函数，用于计算二分类问题的各种性能评估指标。该函数需要计算以下指标：
# 1. 混淆矩阵（Confusion Matrix）
# 2. 准确率（Accuracy）
# 3. F1分数（F1 Score）
# 4. 特异度（Specificity）
# 5. 负预测值（Negative Predictive Value）
# 这些指标在机器学习中用于评估分类模型的性能，特别是在二分类问题中。

# 输入描述：
# 第一行输入实际类别标签列表（1表示正类，0表示负类）。
# 第二行输入模型预测的类别标签列表（1表示正类，0表示负类）。

# 输出描述：
# 返回一个包含以下五个元素的元组：
# 1. confusion_matrix：2×2的混淆矩阵，格式为[[TN, FP], [FN, TP]]
# 2. accuracy：模型的准确率（保留3位小数）
# 3. f1_score：F1分数（保留3位小数）
# 4. specificity：特异度（保留3位小数）
# 5. negative_predictive_value：负预测值（保留3位小数）

# - 准确率 (Accuracy)：
#       $$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
# - F1分数 (F1 Score)：
#       $$F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$$
#   其中：精确率 (Precision)：
#       $Precision = \frac{TP}{TP + FP}$
# - 召回率 (Recall)：
#       $Recall = \frac{TP}{TP + FN}$
# - 特异度 (Specificity)：
#       $$Specificity = \frac{TN}{TN + FP}$$
# - 负预测值 (Negative Predictive Value)：
#       $$Negative Predictive Value = \frac{TN}{TN + FN}$$

# 输入：
# [1, 0, 1, 1, 0, 1]
# [1, 0, 1, 0, 0, 1]

# 输出：
# ([[3, 1], [0, 2]], 0.833, 0.857, 1.0, 0.667)

from collections import Counter

def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    metric = Counter((i, j) for i, j in zip(actual, predicted))
    TP, TN, FN, FP = metric[1, 1], metric[0, 0], metric[1, 0], metric[0, 1]
    confusion_matrix = [[TP, FN], [FP, TN]]
    accuracy = (TP + TN) / (TP + TN + FN + FP)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = 2 * (precision * recall) / (precision + recall)
    specificity = TN / (TN + FP)
    negativePredictive = TN / (TN + FN)

    return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)


if __name__ == "__main__":
    actual = eval(input())
    predicted = eval(input())
    print(performance_metrics(actual, predicted))