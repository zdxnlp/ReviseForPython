def coin_change(coins: list[int], amount: int) -> int:
    # Step 1: 定义状态
    # dp[j] 表示凑出金额 j 的最少硬币数
    dp = [float("inf")] * (amount + 1)

    # Step 2: 初始化
    dp[0] = 0

    # Step 3: 完全背包正序递推
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # Step 4: 返回答案
    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))
