# LeetCode 总结

个人 LeetCode 刷题总结，按题型分类整理解题思路与代码模板。

## 目录

- [动态规划 (Dynamic Programming)](#动态规划-dynamic-programming)

---

## 动态规划 (Dynamic Programming)

| # | 题目 | 难度 | 状态 |
| --- | --- | --- | --- |
| 70 | 爬楼梯 | 简单 | ⬜ |
| 118 | 杨辉三角 | 简单 | ⬜ |
| 198 | 打家劫舍 | 中等 | ⬜ |
| 279 | 完全平方数 | 中等 | ⬜ |
| 322 | [零钱兑换](#322-零钱兑换) | 中等 | ✅ |
| 139 | 单词拆分 | 中等 | ⬜ |
| 300 | 最长递增子序列 | 中等 | ⬜ |
| 152 | 乘积最大子数组 | 中等 | ⬜ |
| 416 | 分割等和子集 | 中等 | ⬜ |
| 32 | 最长有效括号 | 困难 | ⬜ |

---

### 322. 零钱兑换

**题目**：给定不同面额的硬币数组 `coins` 和总金额 `amount`，返回凑成总金额所需的**最少**硬币个数；无解返回 `-1`。每种硬币数量无限。

**思路**：完全背包问题。定义 `dp[i]` 为凑出金额 `i` 所需的最少硬币数。

- **状态转移**：对每个金额 `i`,遍历所有硬币 `coin`，若 `i - coin >= 0`，则 `dp[i] = min(dp[i], dp[i-coin] + 1)`
- **初始化**：`dp[0] = 0`（金额 0 无需硬币），其余设为极大值（如 `1e8`）作为"不可达"标记
- **返回**：`dp[amount]` 仍为极大值说明无解返回 `-1`，否则返回 `dp[amount]`

**复杂度**：时间 `O(amount × len(coins))`，空间 `O(amount)`。

**代码**：

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e8] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return -1 if dp[amount] == 1e8 else dp[amount]
```

**要点**：
- 外层遍历金额、内层遍历硬币 → 求"最少个数"顺序无关，两种循环顺序都可
- 若问题变成"凑出金额的组合数"（硬币顺序不敏感），必须外层遍历硬币、内层遍历金额
- 哨兵值推荐用 `amount + 1`（一定不可达），比 `1e8` 更严谨且避免浮点
