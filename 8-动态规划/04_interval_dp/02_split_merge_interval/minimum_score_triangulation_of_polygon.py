def min_score_triangulation(values: list[int]) -> int:
    n = len(values)

    # Step 1: 定义状态
    # dp[i][j] 表示区间 [i, j] 的最低三角剖分得分
    dp = [[0] * n for _ in range(n)]

    # Step 2 and 3: 按区间长度递推
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float("inf")
            for k in range(i + 1, j):
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][k] + dp[k][j] + values[i] * values[k] * values[j],
                )

    # Step 4: 返回答案
    return dp[0][n - 1]


if __name__ == "__main__":
    print(min_score_triangulation([1, 3, 1, 4, 1, 5]))
