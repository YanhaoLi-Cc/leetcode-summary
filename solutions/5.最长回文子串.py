#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len, begin = 1, 0
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)] 
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n + 1):
            for left in range(n):
                right = left + L - 1
                if right >= n:
                    break
                if s[left] != s[right]:
                    dp[left][right] = False
                elif s[left] == s[right]:
                    if L == 2:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left+1][right-1] 
            
                if dp[left][right] and L > max_len:
                    max_len = L
                    begin = left
        return s[begin:begin + max_len]
                
        
# @lc code=end

