def longest_palindrome_subseq(s: str) -> int:
    n = len(s)

    # Step 1: 定义状态
    # dp[i][j] 表示区间 s[i..j] 的最长回文子序列长度
    dp = [[0] * n for _ in range(n)]

    # Step 2: 初始化长度为 1 的区间
    for i in range(n):
        dp[i][i] = 1

    # Step 3: 按区间长度递推
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Step 4: 返回答案
    return dp[0][n - 1]


if __name__ == "__main__":
    print(longest_palindrome_subseq("bbbab"))
