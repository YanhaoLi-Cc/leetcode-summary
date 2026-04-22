# LeetCode 总结

个人 LeetCode 刷题总结，按题型分类整理解题思路与代码模板。

## 目录

- [动态规划 (Dynamic Programming)](#动态规划-dynamic-programming)
- [面试题 (Interview)](#面试题-interview)

---

## 动态规划 (Dynamic Programming)

| # | 题目 | 难度 | 状态 |
| --- | --- | --- | --- |
| 70 | 爬楼梯 | 简单 | ⬜ |
| 118 | 杨辉三角 | 简单 | ⬜ |
| 198 | 打家劫舍 | 中等 | ⬜ |
| 279 | 完全平方数 | 中等 | ⬜ |
| 322 | [零钱兑换](#322-零钱兑换) | 中等 | ✅ |
| 518 | [零钱兑换 II](#518-零钱兑换-ii) | 中等 | ✅ |
| 139 | [单词拆分](#139-单词拆分) | 中等 | ✅ |
| 300 | [最长递增子序列](#300-最长递增子序列) | 中等 | ✅ |
| 152 | [乘积最大子数组](#152-乘积最大子数组) | 中等 | ✅ |
| 416 | [分割等和子集](#416-分割等和子集) | 中等 | ✅ |
| 32 | [最长有效括号](#32-最长有效括号) | 困难 | ✅ |

---

### 322. 零钱兑换

**题目**：给定不同面额的硬币数组 `coins` 和总金额 `amount`，返回凑成总金额所需的**最少**硬币个数；无解返回 `-1`。每种硬币数量无限。

**解法类型**：完全背包 · 最值 DP

**`dp` 定义**：`dp[i]` = 凑出金额 `i` 所需的**最少硬币数**；若无法凑出，保留为"不可达"哨兵。

**状态转移方程**：

$$dp[i] = \min_{coin \in coins,\ i \geq coin}\ \big(dp[i],\ dp[i-coin] + 1\big)$$

语义：凑出 `i` 的最少硬币数 = 在所有"最后一枚选 `coin`"的候选里，取 `dp[i-coin] + 1` 的最小值。

**初始化 / 边界**：
- `dp[0] = 0`（金额 0 无需任何硬币）
- 其余设为"不可达"大值（如 `amount + 1` 或 `1e8`）
- 返回前判断 `dp[amount]` 是否仍为大值：是 → 返回 `-1`，否则返回 `dp[amount]`

**复杂度**：时间 `O(amount × len(coins))`，空间 `O(amount)`。

**代码**：

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e8] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return -1 if dp[amount] == 1e8 else dp[amount]
```

**要点**：
- 外层遍历金额、内层遍历硬币 → 求"最少个数"顺序无关，两种循环顺序都可
- 若问题变成"凑出金额的组合数"（硬币顺序不敏感），必须外层遍历硬币、内层遍历金额
- 哨兵值推荐用 `amount + 1`（一定不可达），比 `1e8` 更严谨且避免浮点

---

### 518. 零钱兑换 II

**题目**：给定不同面额的硬币数组 `coins` 和总金额 `amount`，返回可以凑成总金额的**硬币组合数**。每种硬币数量无限，`[1,2]` 与 `[2,1]` 视为同一种组合。

**解法类型**：完全背包 · 计数 DP

**`dp` 定义**：`dp[i]` = 用给定硬币凑出金额 `i` 的**组合数**（顺序不敏感）。

**状态转移方程**（一维滚动形式，按硬币逐个累加）：

$$dp[i]\ \mathrel{+}=\ dp[i - coin],\qquad \forall\ coin \in coins,\ i \geq coin$$

语义：凑出 `i` 的组合数 = 累加所有"最后一枚放 `coin`"的方案数；按硬币顺序引入天然去重了排列。

**初始化 / 边界**：
- `dp[0] = 1`（凑出金额 0 有 1 种方案：什么都不选，作为计数基准）
- 其余为 `0`
- **循环顺序必须外层硬币、内层金额**——否则变成排列数，`1+2` 与 `2+1` 会分别计数
- 无解无需特判：`dp[amount] = 0` 即 0 种

**复杂度**：时间 `O(amount × len(coins))`，空间 `O(amount)`。

**代码**：

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)  # dp[i] = 用给定硬币凑出金额 i 的方案数
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
```

**要点**：
- `dp[0] = 1` 是计数型 DP 的关键基准，代表"空选"算 1 种方案；若为 0，后续累加全部失效
- 循环顺序若调换（外层金额、内层硬币）则变成求**排列数**，`1+2` 与 `2+1` 会分别计数
- `dp[i] += dp[i-coin]` 用的是"处理完当前硬币后的一维滚动数组"，省去二维 `dp[j][i]`

---

### 322 vs 518 对比

两题外形一致（同样的 `coins` + `amount`），但问的东西不同，DP 的每个要素都要跟着变：

| 维度 | 322 零钱兑换 | 518 零钱兑换 II |
| --- | --- | --- |
| 问的是 | 最少硬币个数（最值） | 组合方案数（计数） |
| `dp[i]` 含义 | 凑出 `i` 的最少硬币数 | 凑出 `i` 的组合数 |
| 初始化 | `dp[0]=0`，其余为"不可达"大值 | `dp[0]=1`，其余为 `0` |
| 状态转移 | `dp[i] = min(dp[i], dp[i-coin] + 1)` | `dp[i] += dp[i-coin]` |
| 循环顺序 | 两种都可（min 与顺序无关） | 必须外层硬币、内层金额 |
| 无解处理 | `dp[amount]` 仍为大值 → 返回 -1 | 无需特判，`dp[amount]=0` 即 0 种 |

**一句话总结**：**最值 DP** 看的是路径上的成本，顺序不影响谁最小；**计数 DP** 看的是路径的身份，循环顺序直接决定把"同一组合的不同顺序"算一次还是多次。

---

### 139. 单词拆分

**题目**：给定字符串 `s` 和字符串列表 `wordDict`，判断 `s` 是否能被拆分成若干字典中出现的单词（单词可重复使用，不要求用完所有单词）。

**解法类型**：字符串划分 · 布尔型 DP

**`dp` 定义**：`dp[i]` = 字符串 `s` 的前 `i` 个字符 `s[0:i]` 能否被字典里的单词完整拼出（布尔值）。注意 `i` 是**前缀长度**而非索引，范围 `0..len(s)`。

**状态转移方程**：

$$dp[j] = \bigvee_{0 \leq i < j}\ \big(dp[i]\ \wedge\ s[i:j] \in wordDict\big)$$

语义：`s[0:j]` 能拼出 ⟺ 存在切分点 `i`，使得左段 `s[0:i]` 已能拼出且右段 `s[i:j]` 恰好是字典里的单词。

**初始化 / 边界**：
- `dp[0] = True`（空串作为递推基准，天然"能拼出"）
- 其余为 `False`
- 返回 `dp[len(s)]`

**复杂度**：时间 `O(n² · L)`（`n = len(s)`，`L` 为单词平均长度，来自 `s[i:j]` 切片 + `in` 查找），空间 `O(n)`。

**代码**：

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)  # dp[i]: s[0:i] 能否被字典单词拼出
        dp[0] = True
        for i in range(N):
            for j in range(i + 1, N + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[N]
```

**要点**：
- **易错点 1**：循环里必须检查 `dp[i]`（左段已可拼），写成 `s[i]` 会让判断失效（字符永远 truthy），遇到 `"catsandog"` 这类反例就会误判
- **易错点 2**：`dp[j] = True` 是赋值，别误写成 `dp[j] == True`（这是比较，返回值被丢弃，`dp` 永远全 False）
- **性能优化**：`wordDict` 先转 `set`，把 `in` 查找从 `O(len(wordDict)·L)` 降到 `O(L)`
- **剪枝**：内层找到一个切分点即可 `break`（`dp[j]` 已为 True，继续检查多余）

---

### 300. 最长递增子序列

**题目**：给定整数数组 `nums`，返回最长**严格递增子序列**的长度。子序列允许删除任意元素，但保留原顺序。

**解法类型**：子序列 DP · 以位置结尾

**`dp` 定义**：`dp[i]` = **以 `nums[i]` 结尾**的最长严格递增子序列的长度。关键约束——`nums[i]` 必须是该子序列的**最后一个元素**，这样 `dp[j]` 才能推出"能否把 `nums[i]` 接上去"。

**状态转移方程**：

$$dp[i] = \max\Big(1,\ \max_{0 \leq j < i,\ nums[j] < nums[i]}\ dp[j] + 1\Big)$$

语义：以 `nums[i]` 结尾的 LIS = 找一个位置 `j < i` 满足 `nums[j] < nums[i]`，把 `nums[i]` 接在以 `nums[j]` 结尾的 LIS 后面；若没有可接的 `j`，则 `nums[i]` 自成一串长度 1。

**初始化 / 边界**：
- `dp[i] = 1`（每个元素至少自成一个长度为 1 的子序列）
- 严格递增 ⇒ 判断用 `<` 而非 `<=`
- **答案是 `max(dp)` 而非 `dp[N-1]`**——LIS 可以在任意位置结束

**复杂度**：时间 `O(N²)`，空间 `O(N)`。

**代码**：

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N   # dp[i]: 以 nums[i] 结尾的最长严格递增子序列长度
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```

**要点**：
- **易错点 1**：返回值必须是 `max(dp)`，写成 `dp[N-1]` 在 `[1,2,3,0]` 这种数据上会错（末位不是 LIS 终点）
- **易错点 2**：严格递增是 `<`，若题目改为非严格递增则改成 `<=`
- **为什么定义成"以 `i` 结尾"**：转移需要知道"上一个元素的值"才能判断是否可接；若定义成"前 `i+1` 个数的任意 LIS"，`dp[j]` 那条子序列的结尾未知，根本无法转移
- **进阶 O(N log N)**：维护一个 `tails` 数组（`tails[k]` 表示长度为 `k+1` 的所有递增子序列中最小的末尾值），用 `bisect_left` 找插入位置；数据到 `N ≤ 10⁵` 时必须用此解法
- **同类套路**：53 最大子数组和、152 乘积最大子数组、32 最长有效括号，都采用"以 `i` 结尾"的状态定义 + `max(dp)` 收尾

---

### 152. 乘积最大子数组

**题目**：给定整数数组 `nums`，返回**连续子数组**的最大乘积。

**解法类型**：子数组 DP · 双状态（最大 + 最小）

**`dp` 定义**：
- `dp_max[i]` = 以 `nums[i]` 结尾的连续子数组的**最大**乘积
- `dp_min[i]` = 以 `nums[i]` 结尾的连续子数组的**最小**乘积

**为什么要双 DP**：遇到负数时，最小（负得最多）乘以负数会翻身变成最大，所以必须同时维护。

**状态转移方程**：

$$dp_{max}[i] = \max\big(nums[i],\ dp_{max}[i-1] \cdot nums[i],\ dp_{min}[i-1] \cdot nums[i]\big)$$

$$dp_{min}[i] = \min\big(nums[i],\ dp_{max}[i-1] \cdot nums[i],\ dp_{min}[i-1] \cdot nums[i]\big)$$

三个候选：自己单起（切断前面）、乘前 max、乘前 min。

**初始化 / 边界**：`dp_max[0] = dp_min[0] = nums[0]`；答案是 `max(dp_max)`。

**复杂度**：时间 `O(N)`，空间 `O(N)`（可优化到 `O(1)`）。

**代码**：

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        dp_max, dp_min = [0] * N, [0] * N
        dp_max[0], dp_min[0] = nums[0], nums[0]
        for i in range(1, N):
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(nums[i], dp_min[i-1] * nums[i], dp_max[i-1] * nums[i])
        return max(dp_max)
```

**要点**：
- 与 300 LIS 的区别：**连续子数组** ⇒ 只依赖 `dp[i-1]`，无需内层循环；**负数** ⇒ 必须同时维护 max 和 min
- `nums[i]` 作为候选之一，等价于"遇到 0 或不利乘积时从当前位置重新开始"
- `O(1)` 空间优化：用 `cur_max`、`cur_min` 两个变量替代数组，但更新时要先缓存旧值，防止 `cur_max` 被覆盖后污染 `cur_min` 的计算

---

### 416. 分割等和子集

**题目**：给定只含正整数的非空数组 `nums`，判断能否分成两个元素和相等的子集。

**解法类型**：0/1 背包 · 存在型 DP

**问题转化**：两子集和相等 ⇒ 每个子集和为 `total // 2`。问题等价于"**能否从 `nums` 中选出若干元素，使和恰好等于 `target = total // 2`**"——经典 0/1 背包。

**`dp` 定义**：`dp[i][j]` = 从前 `i+1` 个元素（索引 `0..i`）中，**能否选出一个子集**使其和恰好为 `j`（存在型，不要求包含 `nums[i]`）。

**状态转移方程**（代码形式）：

```python
# 不选 nums[i]
dp[i][j] = dp[i-1][j]
# 选 nums[i]（与"不选"取 or 合并）
if j == nums[i]:
    dp[i][j] = True
elif j > nums[i]:
    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i]]
```

**初始化 / 边界**：
- `total` 为奇数 → 直接返回 `False`
- `nums[0] > target` → 直接返回 `False`（否则 `dp[0][nums[0]]` 越界）
- `dp[0][nums[0]] = True`，其余 `False`
- 答案：`dp[N-1][target]`

**复杂度**：时间 `O(N × target)`，空间 `O(N × target)`（可压一维到 `O(target)`）。

**代码**：

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        if nums[0] > target:
            return False

        # dp[i][j]: 前 i+1 个元素能否凑出和 j
        dp = [[False] * (1 + target) for _ in range(N)]
        dp[0][nums[0]] = True
        for i in range(1, N):
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j]                        # 不选
                if j == nums[i]:
                    dp[i][j] = True                          # 选（单独够）
                elif j > nums[i]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i]]  # 选（和之前拼）
        return dp[N-1][target]
```

**要点**：
- **易错点**：情况 2.2 必须用 `or` 和情况 1 合并，写成 `=` 会把"不选"的 True 结果覆盖掉，酿成 `[3,1,4,2,2]` 这类反例错误
- **"存在型" vs "以 i 结尾"**：本题 `dp[i][j]` 不要求包含 `nums[i]`（子集能凑出即可），所以答案是 `dp[N-1][target]` 这个固定格子；对比 300 LIS/152 乘积最大子数组必须"以 `i` 结尾"，答案要 `max(dp)`
- **0/1 背包 vs 完全背包**：本题每个元素只能用一次（0/1）；322/518 的硬币可无限次（完全）。一维压缩时，0/1 背包内层**倒序**，完全背包内层**正序**
- **一维优化**：`dp = [False] * (target + 1); dp[0] = True`，内层 `for j in range(target, num - 1, -1)` 倒序更新

---

### 32. 最长有效括号

**题目**：给定只含 `(` 和 `)` 的字符串 `s`，返回最长**有效且连续**括号子串的长度。

**解法类型**：字符串 DP · 以位置结尾

**`dp` 定义**：`dp[i]` = 以 `s[i]` 结尾的最长有效括号子串长度（必须以 `s[i]` 结尾；`s[i]='('` 时必为 0，因有效子串必以 `)` 收尾）。

**状态转移方程**（代码形式）：

```python
# s[i] == '(' 时 dp[i] = 0
# s[i] == ')' 时，令 match = i - dp[i-1] - 1（理论上应配对的 '(' 位置）
if match >= 0 and s[match] == '(':
    dp[i] = dp[i-1] + 2 + dp[match - 1]
    #       └──┬──┘  └┬┘  └─────┬─────┘
    # 以 i-1 结尾的段  新配的一对   match 之前已有的有效段
```

**两种情形统一在一条公式里**：
- `s[i-1] = '('`：`dp[i-1] = 0`，公式退化为 `dp[i-2] + 2`，对应直接配对 `"()"`
- `s[i-1] = ')'`：跨过以 `s[i-1]` 结尾的整段去找匹配 `(`，对应嵌套 `"...))"`

**初始化 / 边界**：全 `0`；答案是 `max(dp)`（有效子串可在任意位置结束）。

**复杂度**：时间 `O(N)`，空间 `O(N)`。

**代码**：

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 1)   # dp[i]: 以 s[i] 结尾的最长有效括号长度
        for i in range(1, N):
            if s[i] == ')' and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = dp[i - dp[i-1] - 2] + dp[i-1] + 2
        return max(dp) if dp else 0
```

**要点**：
- **易错点 1**：条件顺序要把**边界检查 `match >= 0` 前置**，否则先访问 `s[-1]` 会因 Python 负索引拿到末字符，造成假匹配
- **易错点 2**：返回 `max(dp)` 而非 `dp[N-1]`——"以 `i` 结尾"型 DP 的通用模式
- **`dp[-1]` 的巧合**：`dp = [0] * (N+1)` 多开一格保证 `dp[-1] = dp[N] = 0`，让 `dp[i-dp[i-1]-2]` 在下标为 `-1` 时也返回 `0`；改用 `dp = [0] * N` 要显式判断 `match - 1 >= 0`
- **同类套路**：300 LIS、152 乘积最大子数组，都是"以 `i` 结尾 + `max(dp)` 收尾"

---

## 面试题 (Interview)

| 题目 | 来源 | 类型 | 状态 |
| --- | --- | --- | --- |
| [卷子分数](#卷子分数华为机试) | 华为机试 2022-04-20 | 带停止条件的计数 DP | ✅ |

---

### 卷子分数（华为机试）

**题目**：一张试卷共 25 题（10 道单选 2 分、10 道填空 4 分、5 道多选 8 分，按顺序作答）。答题时连续出现 3 道错题就停止考试并记录当前分数。给定分数 `N`，问最多有多少种答题情况。

**来源**：[LeetCode 讨论区 · 4.20 华为机试](https://leetcode.cn/discuss/post/3564551/)

**解法类型**：带停止条件的计数 DP · 三维状态

**`dp` 定义**：`dp[i][j][k]` = 答完前 `i` 题、当前分数为 `j`、末尾连续 `k` 道错题（`k ∈ {0, 1, 2}`）、尚未触发 3 连错停止 的方案数。

**为什么要三维**：
- `i`：题号（决定当前是第几题，影响分值）
- `j`：分数（题目问的统计维度）
- `k`：末尾连续错题数（决定下一次答错是否触发停止）

"末尾连续错题数"是**必须入状态**的维度——不记录的话，无从判断下一道错题是否触发停止。

**状态转移方程**（push 风格）：

```python
# 答对：分数 +p，连续错清零
dp[i+1][j + p][0] += dp[i][j][k]

# 答错 (k < 2)：分数不变，连续错 +1
dp[i+1][j][k + 1] += dp[i][j][k]

# 答错 (k == 2)：触发 3 连错，考试停止，分数 j 被记录
stopped[j] += dp[i][j][k]
```

**初始化 / 边界**：
- `dp[0][0][0] = 1`（未答题、0 分、0 连错）
- `stopped[s]` 记录"任意位置触发停止、最终分数为 s"的方案数
- **答案**：`ans(N) = Σ_k dp[25][N][k] + stopped[N]`（完成整卷的方案 + 中途停止的方案）

**复杂度**：时间 `O(len × max_score × 3)`，即 `25 × 101 × 3 ≈ 7600`；空间同阶（可滚动压成 `O(max_score × 3)`）。

**代码**：

```python
class Solution:
    def countScenarios(self, N: int, points: list) -> int:
        lens = len(points)
        max_score = sum(points)
        # dp[i][j][k]: 答完前 i 题、分数 j、末尾连续 k 错、未停止的方案数
        dp = [[[0] * 3 for _ in range(max_score + 1)] for _ in range(lens + 1)]
        dp[0][0][0] = 1
        stopped = [0] * (max_score + 1)

        for i in range(lens):
            point = points[i]
            for j in range(max_score + 1):
                for k in range(3):
                    cnt = dp[i][j][k]
                    if cnt == 0:
                        continue
                    # 答对
                    if j + point <= max_score:
                        dp[i + 1][j + point][0] += cnt
                    # 答错
                    if k < 2:
                        dp[i + 1][j][k + 1] += cnt
                    else:
                        stopped[j] += cnt

        completed = sum(dp[lens][N][k] for k in range(3))
        return completed + stopped[N]
```

**要点**：
- **push vs pull**：代码是 push 风格——"从当前状态把方案数推到未来"；同一目标被多个来源贡献，**必须用 `+=` 累加**，写 `=` 会被后续的 `k` 循环覆盖
- **三维 vs 滚动压缩**：逻辑上是 `dp[i][j][k]`，代码里 `i` 维度可以用两层数组滚动压掉，空间从 `O(I×S×K)` 降到 `O(S×K)`；初学调试建议保留三维
- **"停止"不是 dp 的一个格子**：考试停止后就不再有后续状态，单独用 `stopped[j]` 累加
- **同类套路**：带终止条件的计数问题（如"连续 k 次事件就结束"），通用解法都是"把末尾连续计数 k 放进状态"
