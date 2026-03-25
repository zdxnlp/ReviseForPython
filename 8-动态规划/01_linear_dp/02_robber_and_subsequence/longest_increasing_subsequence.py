def length_of_lis(nums: list[int]) -> int:
    if not nums:
        return 0

    # Step 1: 定义状态
    # dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
    dp = [1] * len(nums)

    # Step 2 and 3: 初始化已经体现在 dp 全部设为 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Step 4: 返回全局最优
    return max(dp)


if __name__ == "__main__":
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
