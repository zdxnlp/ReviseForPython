"""
本题目：寻找序列中和为M的子序列总数。
问：如果要求解的是子序列，又因该如何做

去重！如何做？
"""
"""
dp[i][j]:前i个所有组合中，和为j的 组合数
以i为结束：
    dp[i][j] = dp[i-1][j-v[i]]
不以i结束：
    dp[i][j] = dp[i-1][j]
"""

def solution():
    l = int(input())
    v = list(map(int,input().split()))
    num = int(input())

    dp = [[0] * (num+1) for _ in range(l+1)]
    dp[0][0] = 1
    for i in range(1,l+1):
        for j in range(num+1):
            dp[i][j] = dp[i-1][j]
            if v[i-1] <= j:
                dp[i][j] += dp[i-1][j-v[i-1]]
    print(dp[l][num])

def solution2():
    """多重背包：相同价值算一种，但可以选多个"""
    _ = int(input())
    v = list(map(int, input().split()))
    num = int(input())

    # 统计每个价值出现的次数
    from collections import Counter
    count = Counter(v)
    values = list(count.keys())
    l = len(values)

    dp = [[0] * (num + 1) for _ in range(l + 1)]
    dp[0][0] = 1

    for i in range(1, l + 1):
        val = values[i-1]
        cnt = count[val]
        for j in range(num + 1):
            # 选择k个当前价值的奖品 (0 <= k <= cnt)
            for k in range(cnt + 1):
                if k * val <= j:
                    dp[i][j] += dp[i-1][j - k * val]

    print(dp[l][num])

def solution3():
    """DFS回溯：输出所有具体组合"""
    _ = int(input())
    v = list(map(int, input().split()))
    num = int(input())

    result = []  # 存储所有组合
    path = []    # 当前路径

    def dfs(index, remain):
        """
        index: 当前考虑第几个奖品
        remain: 还需要凑多少
        """
        if remain == 0:
            result.append(path[:])  # 找到一个组合
            return
        if index >= len(v) or remain < 0:
            return

        # 选择当前奖品
        path.append(v[index])
        dfs(index + 1, remain - v[index])
        path.pop()

        # 不选当前奖品
        dfs(index + 1, remain)

    dfs(0, num)
    print(f"组合数: {len(result)}")
    for combo in result:
        print(combo)

if __name__ == '__main__':
    solution()
    # solution2()  # 取消注释测试去重版本
    # solution3()  # 取消注释测试DFS版本