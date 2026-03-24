# 买卖股票的最佳时机含冷冻期

## 题目

你可以多次交易，但卖出股票后，第二天无法立刻买入，必须经过一天冷冻期，求最大利润。

## 为什么是状态机 DP

除了持股和不持股，还要区分“不持股但刚卖出”和“不持股且可买入”这样的限制状态。

## 四步法

1. 定义状态：
   - `hold`：当天结束后持股
   - `sold`：当天刚卖出
   - `rest`：当天不持股且不在冷冻期
2. 写转移：
   - `hold = max(prev_hold, prev_rest - price)`
   - `sold = prev_hold + price`
   - `rest = max(prev_rest, prev_sold)`
3. 初始化：第一天 `hold = -prices[0]`，`sold = 0`，`rest = 0`。
4. 遍历顺序：按天推进，答案是 `max(sold, rest)`。

## 递推阶梯

- 持股只能由“之前持股”或“今天从可买状态买入”得到
- 刚卖出只能由“昨天持股，今天卖掉”得到
- 可买状态来自“昨天就空仓”或“昨天刚卖出，今天冷冻结束”

## 公式

- `hold = max(prev_hold, prev_rest - price)`
- `sold = prev_hold + price`
- `rest = max(prev_rest, prev_sold)`

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`
