#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        if nums[0] > target:
            return False

        # dp[i][j]表示前i个元素里能不能装满j的背包
        dp = [[False] * (1+target) for _ in range(N)]
        dp[0][nums[0]] = True 
        for i in range(1, N):
            for j in range(1, target + 1):
                # 如果不选nums[i]
                dp[i][j] = dp[i-1][j]
                # 如果选nums[i]
                if j == nums[i]:
                    dp[i][j] = True
                elif j > nums[i]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i]]
        return dp[N-1][target]

# @lc code=end

