def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)

    # Step 1: 定义状态
    # dp[i] 表示到达第 i 阶时的最小花费
    dp = [0] * (n + 1)

    # Step 2: 初始化
    dp[0] = 0
    dp[1] = 0

    # Step 3: 递推
    for i in range(2, n + 1):
        one_step = dp[i - 1] + cost[i - 1]
        two_steps = dp[i - 2] + cost[i - 2]
        dp[i] = min(one_step, two_steps)

    # Step 4: 返回答案
    return dp[n]


if __name__ == "__main__":
    print(min_cost_climbing_stairs([10, 15, 20]))
