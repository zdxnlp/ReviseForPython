def find_target_sum_ways(nums: list[int], target: int) -> int:
    total = sum(nums)
    if total + target < 0 or (total + target) % 2 == 1:
        return 0

    bag = (total + target) // 2

    # Step 1: 定义状态
    # dp[j] 表示凑出和为 j 的方案数
    dp = [0] * (bag + 1)

    # Step 2: 初始化
    dp[0] = 1

    # Step 3: 0/1 背包倒序累加方案数
    for num in nums:
        for j in range(bag, num - 1, -1):
            dp[j] += dp[j - num]

    # Step 4: 返回答案
    return dp[bag]


if __name__ == "__main__":
    print(find_target_sum_ways([1, 1, 1, 1, 1], 3))
