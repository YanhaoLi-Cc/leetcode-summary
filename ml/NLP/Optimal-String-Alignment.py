# 描述
# 实现最优字符串对齐（Optimal String Alignment，OSA）距离的计算。
# OSA距离是衡量两个字符串相似度的指标，表示将一个字符串转换为另一个字符串所需的最小编辑操作次数。

# 允许的编辑操作（每个操作代价为1）：
#   1. 插入一个字符
#   2. 删除一个字符
#   3. 替换一个字符
#   4. 交换相邻的两个字符
# 输入描述：
#   第一行输入源字符串。
#   第二行输入目标字符串。
# 输出描述：
#   返回一个整数，表示从源字符串转换到目标字符串所需的最小操作次数。
# 
# 示例1
# 输入：
# "caper"
# "acer"
# 输出：
# 2

def OSA(source: str, target: str) -> int:
    m, n = len(source), len(target)
    # dp[i][j] 表示 source[:i] 转换为 target[:j] 的最小操作次数
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i # 全部删除
    for j in range(n + 1):
        dp[0][j] = j # 全部插入

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i][j - 1],
                    dp[i - 1][j],
                    dp[i - 1][j - 1]
                ) + 1
            
            # 相邻字符交换：检查 source 和 target 的两个字符是否交叉相等
            if i >= 2 and j >= 2 and source[i - 1] == target[j - 2] and source[i - 2] == target[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)
                
    return dp[m][n]

if __name__ == "__main__":
    source = eval(input())
    target = eval(input())
    print(OSA(source, target))