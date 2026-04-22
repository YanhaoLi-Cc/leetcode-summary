#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        # dp[i]: 以 s[i] 结尾的最长有效括号子串的长度（必须以 s[i] 结尾）
        # s[i] == '(' 时 dp[i] = 0（有效子串必以 ')' 结尾）
        dp = [0] * (N + 1)
        for i in range(1, N):
            # 只有 s[i] == ')' 才可能形成有效配对；
            # match = i - dp[i-1] - 1 表示"跨过以 s[i-1] 结尾的有效段"后，
            # 理论上与 s[i] 配对的左括号所在位置。若该位置确实是 '(' 且没越界，匹配成立。
            if s[i] == ')' and s[i-dp[i-1]-1] == "(" and i-dp[i-1]-1 >= 0:
                # 状态转移方程:
                #   dp[i] = dp[i - dp[i-1] - 2] + dp[i-1] + 2
                #           └────────┬────────┘   └──┬──┘  └┬┘
                #         更前面可接续的有效段       以 i-1      新闭合的这一对
                #         (match '(' 之前的 dp)      结尾的段      '(' 与 s[i]
                #
                # 图示(假设 s[i-1] 是 ')'):
                #   位置:  ... [ match-1 ]  match  [ i-dp[i-1] .. i-1 ]  i
                #   字符:  ... [已有效段]    '('   [ 紧邻 s[i-1] 的有效段 ]  ')'
                #                └ dp[match-1] ┘   └──── dp[i-1] ────┘   └ +2 ┘
                #
                # 特殊情形: s[i-1] == '(' 时 dp[i-1] = 0，
                #   match = i - 1, s[i-1] = '(' 直接配 s[i]，
                #   dp[i] = dp[i-2] + 0 + 2 = dp[i-2] + 2
                #   ——公式自动退化成"()" 直接配对的情况
                dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
        # 有效子串可能在任意位置结束，答案取 dp 数组最大值
        return max(dp)
# @lc code=end

