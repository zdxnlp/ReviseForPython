def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    # Step 1: 定义状态
    # dp[i][j] 表示 word1 前 i 个字符转成 word2 前 j 个字符的最小操作数
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: 初始化空串边界
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Step 3: 递推
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i][j - 1],      # 插入
                    dp[i - 1][j],      # 删除
                    dp[i - 1][j - 1],  # 替换
                ) + 1

    # Step 4: 返回答案
    return dp[m][n]


if __name__ == "__main__":
    print(min_distance("horse", "ros"))
