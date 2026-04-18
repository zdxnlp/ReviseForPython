def solve():
    n = int(input())
    if n <= 0:
        return 0

    nums = list(map(int, input().split()))
    if len(nums) != n:
        return 0

    res = nums[0]  # 当前最大收益
    current_sum = nums[0]  # 当前子数组和

    for i in range(1, n):
        if nums[i] + current_sum < nums[i]:  # 从i开始有更大的收益
            current_sum = nums[i]  # 更新当前子数组和
            res = max(res, nums[i])  # 更新最大收益
        else:
            current_sum += nums[i]
            res = max(res, current_sum)

    return res

if __name__ == '__main__':
    s = solve()
    print(s)