#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        #  dp_max[i] = 以 nums[i] 结尾的连续子数组的最大乘积
        #  dp_min[i] = 以 nums[i] 结尾的连续子数组的最小乘积
        dp_max, dp_min = [0] * N, [0] * N
        dp_max[0], dp_min[0] = nums[0], nums[0]
        for i in range(1, N):
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(nums[i], dp_min[i-1] * nums[i], dp_max[i-1] * nums[i])
        return max(dp_max)
# @lc code=end

