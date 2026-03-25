def num_squares(n: int) -> int:
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    # Step 1: 定义状态
    # dp[j] 表示和为 j 时最少需要多少个完全平方数
    dp = [float("inf")] * (n + 1)

    # Step 2: 初始化
    dp[0] = 0

    # Step 3: 完全背包递推
    for square in squares:
        for j in range(square, n + 1):
            dp[j] = min(dp[j], dp[j - square] + 1)

    # Step 4: 返回答案
    return dp[n]


if __name__ == "__main__":
    print(num_squares(12))
