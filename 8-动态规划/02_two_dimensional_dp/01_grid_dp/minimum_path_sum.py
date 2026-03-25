def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # Step 1: 定义状态
    # dp[i][j] 表示到达 (i, j) 的最小路径和
    dp = [[0] * n for _ in range(m)]

    # Step 2: 初始化
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Step 3: 递推
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    # Step 4: 返回答案
    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
