#
# [自测题] 卷子分数
#
# 题目描述：
# 一张试卷总共 25 题：
#   - 10 道单选题，每题 2 分
#   - 10 道填空题，每题 4 分
#   - 5  道多选题，每题 8 分
# 答题时连续出现三道错题就停止考试，并记录当前分数。
# 假设题目按"单选 → 填空 → 多选"的固定顺序作答。
#
# 问题：对于某个最后分数为 N 时，最多有多少种情况？
#
# 来源：https://leetcode.cn/discuss/post/3564551/-/comments/2838079/
#
# ---
#
# 思路（带停止条件的计数 DP）：
#   状态 dp[i][s][k] = 答完前 i 题、当前分数为 s、末尾连续 k 道错题（k∈{0,1,2}）
#                     且至今尚未触发 3 连错停止 的方案数
#   转移（第 i 题分值 p_i）：
#     答对：dp[i][s + p_i][0] += dp[i-1][s][k]
#     答错 k < 2：dp[i][s][k+1]  += dp[i-1][s][k]
#     答错 k == 2：stopped[s] += dp[i-1][s][2]  （3 连错，考试停止）
#   答案（分数 = N）：
#     ans = Σ_k dp[25][N][k]  +  stopped[N]
#
# 实现用滚动数组压掉题号维度 i。

class Solution:
    def countScenarios(self, N: int, points: list) -> int:
        lens = len(points)
        max_score = sum(points)
        dp = [[[0] * 3  for _ in range(max_score + 1)] for _ in range(lens + 1)] # dp[i][j][k] 答完前i题，分数为j，错k题的方案数
        dp[0][0][0] = 1
        stopped = [0] * (max_score + 1) # 在任意位置触发 3 连错停止、最终分数为 s 的方案数

        for i in range(lens): # 从题目0开始
            point = points[i]
            for j in range(max_score + 1):
                for k in range(3):
                    # 答对
                    if j + point <= max_score:
                        dp[i + 1][j + point][0] += dp[i][j][k]
                    # 答错
                    if k < 2:
                        dp[i + 1][j][k+1] += dp[i][j][k]
                    elif k == 2:
                        stopped[j] += dp[i][j][k]
        completed = sum(dp[lens][N][k] for k in range(3))
        return completed + stopped[N]

if __name__ == "__main__":
    sol = Solution()
    # 分数上限 = 10*2 + 10*4 + 5*8 = 100
    points = [2] * 10 + [4] * 10 + [8] * 5
    for N in [0, 2, 4, 8, 100]:
        print(f"N={N:3d}: {sol.countScenarios(N, points)} 种")
