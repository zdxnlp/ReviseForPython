def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    # Step 1: 定义状态
    # dp[i][j] 表示 text1 前 i 个字符与 text2 前 j 个字符的 LCS 长度
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2 and 3: 初始化为空前缀时为 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 4: 返回答案
    return dp[m][n]


if __name__ == "__main__":
    print(longest_common_subsequence("abcde", "ace"))
