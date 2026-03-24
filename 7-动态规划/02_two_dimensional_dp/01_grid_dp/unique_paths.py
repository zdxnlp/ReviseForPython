def unique_paths(m: int, n: int) -> int:
    # Step 1: 定义状态
    # dp[i][j] 表示走到 (i, j) 的路径数
    dp = [[0] * n for _ in range(m)]

    # Step 2: 初始化第一行和第一列
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Step 3: 递推
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Step 4: 返回答案
    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(unique_paths(3, 7))
