def max_profit_once(prices: list[int]) -> int:
    if not prices:
        return 0

    # Step 1: 定义状态
    # dp[i][0] 表示第 i 天结束后不持股的最大利润
    # dp[i][1] 表示第 i 天结束后持股的最大利润
    dp = [[0, 0] for _ in range(len(prices))]

    # Step 2: 初始化
    dp[0][0] = 0
    dp[0][1] = -prices[0]

    # Step 3: 状态转移
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], -prices[i])

    # Step 4: 返回答案
    return dp[-1][0]


if __name__ == "__main__":
    print(max_profit_once([7, 1, 5, 3, 6, 4]))
