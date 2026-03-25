def count_substrings(s: str) -> int:
    n = len(s)

    # Step 1: 定义状态
    # dp[i][j] 表示区间 s[i..j] 是否是回文串
    dp = [[False] * n for _ in range(n)]
    ans = 0

    # Step 2 and 3: 按区间顺序递推并统计答案
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
                ans += 1

    # Step 4: 返回答案
    return ans


if __name__ == "__main__":
    print(count_substrings("aaa"))
