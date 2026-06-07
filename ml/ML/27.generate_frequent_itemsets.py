# 描述
# 频繁项集是指在交易数据中出现频率超过指定阈值的项集，常用于关联规则挖掘，尤其常见于Apriori算法。
# 输入描述：
# - 第一行包含一个整数T，表示交易的数量。
# - 接下来的T行，每行包含一个交易数据，交易数据由一组项组成，项之间用逗号分隔。项用英文小写字母的字符串表示。
# - 最后一行包含一个整数min_support，表示频繁项集出现次数的阈值，用于过滤频繁项集。
# 输出描述：
# 输出所有频繁项集，每个项集以逗号分隔，并按出现频率从高到低排序。每个频繁项集的输出格式为：
# {项1, 项2, ..., 项N}，其中N为项集的大小。

# 输入：
# 2
# eggs,diaper,diaper
# bread,bread,apple,milk,milk
# 1

# 输出：
# {diaper}
# {bread}
# {milk}
# {eggs}
# {apple}
# {eggs, diaper}


from itertools import combinations
from collections import defaultdict

def generate_frequent_itemsets(transactions, min_support):
    return frequent_itemsets

# 主程序
T = int(input())
transactions = [input().strip().split(',') for _ in range(T)]

min_support = int(input())

frequent_itemsets = generate_frequent_itemsets(transactions, min_support)

# 输出结果
for itemset, count in sorted(frequent_itemsets.items(), key=lambda x: -x[1]):
    if isinstance(itemset, str):
        print(f'{{{itemset}}}')
    else:
        print(f'{{{", ".join(itemset)}}}')