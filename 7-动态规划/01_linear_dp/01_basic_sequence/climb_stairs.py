def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    # Step 1: 定义状态
    # dp[i] 表示到达第 i 阶的方法数
    dp = [0] * (n + 1)

    # Step 2: 初始化最小子问题
    dp[1] = 1
    dp[2] = 2

    # Step 3: 按依赖顺序递推
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # Step 4: 返回答案
    return dp[n]


if __name__ == "__main__":
    print(climb_stairs(5))
