#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1) #  字符串 s 的前 i 个字符 s[0:i] 能否被字典里的单词完整拼出
        dp[0] = True
        for i in range(N):
            for j in range(i + 1, N + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[N]
# @lc code=end

