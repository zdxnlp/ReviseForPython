def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 == 1:
        return False

    target = total // 2

    # Step 1: 定义状态
    # dp[j] 表示和 j 是否可以由前面的数字凑出
    dp = [False] * (target + 1)

    # Step 2: 初始化
    dp[0] = True

    # Step 3: 0/1 背包倒序递推
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    # Step 4: 返回答案
    return dp[target]


if __name__ == "__main__":
    print(can_partition([1, 5, 11, 5]))
