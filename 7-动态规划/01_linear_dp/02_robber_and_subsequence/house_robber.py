def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # Step 1: 定义状态
    # dp[i] 表示处理到第 i 间房时的最大收益
    dp = [0] * len(nums)

    # Step 2: 初始化
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Step 3: 递推
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    # Step 4: 返回答案
    return dp[-1]


if __name__ == "__main__":
    print(rob([2, 7, 9, 3, 1]))
