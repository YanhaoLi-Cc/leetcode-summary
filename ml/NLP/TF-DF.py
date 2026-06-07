# 实现一个函数来计算TF-IDF（词频-逆文档频率）分数。TF-IDF是一种用于信息检索和文本挖掘的常用加权技术，用于评估一个词对于文档集中的某个文档的重要程度。
# 输入描述：
# 函数接收两个参数：
# 1. corpus：文档集合，是一个二维列表，每个元素是一个文档（词语列表）
# 2. query：查询词列表，需要计算这些词的TF-IDF分数
# 输出描述：
# 返回一个二维列表，表示每个查询词在每个文档中的TF-IDF分数：
# - 行数等于文档数
# - 列数等于查询词数
# - 结果保留5位小数
# - 按照文档顺序和查询词顺序排列

# TF-IDF是一种衡量文本特征的指标，常用于文本分类和信息检索。其计算公式为：
# TF-IDF = TF * IDF 其中，TF是词频，IDF是逆文档频率。 
# TF的计算公式为：
# TF = 词频 / 文档长度
# IDF 计算公式为：
# IDF = ln(文档总数 + 1 / 包含该词的文档数 + 1) + 1

# 示例1
# 输入：
# [["hello", "world"], ["hello", "python"]]
# ["hello", "python"]
# 输出：
# [[0.5, 0.0], [0.5, 0.70273]]

import math

def compute_tf_idf(corpus, query):
    n_docs = len(corpus) # 文档数量
    result = []

    for doc in corpus:
        row = []
        doc_len = len(doc)
        for word in query:
            # TF = 词在文档中出现的次数 / 文档长度
            tf = doc.count(word) / doc_len if doc_len > 0 else 0
            # DF = 包含该词的文档数
            df = sum(1 for doc in corpus if word in doc)
            # IDF = ln((文档总数 + 1) / (包含该词的文档数 + 1)) + 1
            idf = math.log((n_docs + 1) / (df + 1)) + 1
            # TF-IDF = TF * IDF，保留5位小数
            row.append(round(tf * idf, 5))
        result.append(row)
    return result

if __name__ == "__main__":
    corpus = eval(input())
    query = eval(input())
    print(compute_tf_idf(corpus, query))