def max_coins(nums: list[int]) -> int:
    points = [1] + nums + [1]
    n = len(points)

    # Step 1: 定义状态
    # dp[i][j] 表示开区间 (i, j) 全部戳完的最大收益
    dp = [[0] * n for _ in range(n)]

    # Step 2 and 3: 按区间长度递推
    for length in range(2, n):
        for i in range(0, n - length):
            j = i + length
            for k in range(i + 1, j):
                dp[i][j] = max(
                    dp[i][j],
                    dp[i][k] + dp[k][j] + points[i] * points[k] * points[j],
                )

    # Step 4: 返回答案
    return dp[0][n - 1]


if __name__ == "__main__":
    print(max_coins([3, 1, 5, 8]))
