# 实现一个基于信息增益的决策树学习算法。该算法使用递归的方式构建决策树，通过计算熵和信息增益来选择最优的特征进行数据集划分。

# $$H(S) = - \sum_{i=1}^{c} p_i \log_2(p_i)$$
# 其中，$H(S)$ 是熵，$c$ 是类别的数量，$p_i$ 是属于类别 $i$ 的样本比例。

# $$IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$$
# 其中，$IG(S, A)$ 是信息增益，$Values(A)$ 是属性 $A$ 的所有可能取值，$S_v$ 是在属性 $A$ 取值为 $v$ 时的样本子集。
# H为熵的计算公式；IG为信息增益的计算公式

# **输入描述：**
# 函数接收3个参数：
# 1. examples：列表，包含多个字典，每个字典表示一个训练样本
# 2. attributes：列表，包含可用于划分的属性名
# 3. target_attr：字符串，表示目标属性（类别标签）的名称

# **输出描述：**
# 返回一个嵌套字典，表示学习到的决策树结构：
# * 内部节点：`{属性名: {属性值: 子树, ...}}`
# * 叶节点：直接返回类别值

# 输入
# [{"outlook": "sunny", "temp": "hot", "humidity": "high", "windy": "false", "play": "no"},{"outlook": "sunny", "temp": "hot", "humidity": "high", "windy": "true", "play": "no"},{"outlook": "overcast", "temp": "hot", "humidity": "high", "windy": "false", "play": "yes"},{"outlook": "rain", "temp": "mild", "humidity": "high", "windy": "false", "play": "yes"}]
# ["outlook", "temp", "humidity", "windy"]
# "play"
# 输出
# {outlook:{overcast:yes,rain:yes,sunny:no}}

import math
from collections import Counter

def calculate_entropy(labels):
    """计算标签集合的熵 H(S) = -Σ p_i * log2(p_i)"""
    label_counts = Counter(labels)
    total_count = len(labels)
    entropy = -sum(
        (count / total_count) * math.log2(count / total_count) for count in label_counts.values()
    )
    return entropy

def calculate_information_gain(examples, attr, target_attr):
    """计算属性 attr 的信息增益 IG(S, A) = H(S) - Σ(|S_v|/|S|) * H(S_v)"""
    total_entropy = calculate_entropy([example[target_attr] for example in examples])
    values = set(example[attr] for example in examples)
    attr_entropy = 0
    for value in values:
        # 按属性值划分后的标签子集
        value_subset = [example[target_attr] for example in examples if example[attr] == value]
        attr_entropy += (len(value_subset) / len(examples)) * calculate_entropy(value_subset)
    return total_entropy - attr_entropy

def majority_class(examples, target_attr):
    """返回样本中出现次数最多的类别标签"""
    return Counter([example[target_attr] for example in examples]).most_common(1)[0][0]

def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    """
    ID3 决策树学习算法，基于信息增益选择最优划分属性。
    返回嵌套字典：内部节点为 {属性名: {属性值: 子树}}，叶节点直接返回类别值。
    """
    # 无样本可划分（仅初始为空时触发）
    if not examples:
        return "No examples"
    # 所有样本类别一致，返回该类别作为叶节点
    if len({e[target_attr] for e in examples}) == 1:
        return examples[0][target_attr]
    # 无可用属性，返回多数类别
    if not attributes:
        return majority_class(examples, target_attr)

    # 计算各属性的信息增益，选择最优划分属性
    gains = {attr: calculate_information_gain(examples, attr, target_attr) for attr in attributes}
    best_attr = max(gains, key=gains.get)
    tree = {best_attr: {}}

    # 按最优属性的每个取值划分子集，递归构建子树
    for value in set(example[best_attr] for example in examples):
        subset = [example for example in examples if example[best_attr] == value]
        new_attributes = [a for a in attributes if a != best_attr]
        tree[best_attr][value] = learn_decision_tree(subset, new_attributes, target_attr)

    return tree

def print_tree(tree):
    """将决策树字典格式化为题目要求的输出字符串"""
    outs = []
    for key, value in sorted(tree.items()):
        outs.append(f"{key}:{print_tree(value) if isinstance(value, dict) else value}")
    return "{" + ",".join(outs) + "}"

if __name__ == "__main__":
    examples = eval(input())
    attributes = eval(input())
    target_attr = eval(input())
    print(print_tree(learn_decision_tree(examples, attributes, target_attr)))
