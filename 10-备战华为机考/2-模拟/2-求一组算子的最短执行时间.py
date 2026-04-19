"""
部署在向量单元的算子必须是原数组中一段连续的子数组，每个算子只能二选一部署。由此可以将问题简化为：
    1.设连续部署在向量单元的算子和为s，数组总和为sum_total
    2.矩阵单元总耗时：sum_total - s（未部署在向量的算子全部在矩阵单元）
    3.向量单元总耗时：6 * s（向量单元的耗时是矩阵单元的 6 倍）
    4.总耗时为max(sum_total - s, 6*s)，我们的目标是找到所有合法的s（连续子数组的和，包括s=0，即不部署任何算子到向量单元），使得总耗时最小。
数学推导：
    总耗时函数max(A - s, 6s)（A=sum_total）是一个先减后增的凸函数，
    最小值出现在A - s = 6s，即s = A/7处。因此，我们只需要找到所有连续子数组的和中，最接近A/7的s，即可得到最小总耗时。

解决方案：
    由于数组元素都是正整数，前缀和数组pre_sum是严格递增的，因此可以用「前缀和 + 二分查找」高效求解：
    1.计算前缀和数组pre_sum，pre_sum[0]=0，pre_sum[i]为前i个算子的耗时和。
    2.遍历每个右边界r，对于每个r，我们需要找左边界l < r，使得pre_sum[r] - pre_sum[l]最接近target=A/7，等价于找pre_sum[l]最接近pre_sum[r] - target。
    3.利用前缀和的严格递增性，用二分查找快速定位最接近的pre_sum[l]，计算对应的总耗时，更新全局最小值。
    4.初始最小值设为sum_total，对应s=0（所有算子都部署在矩阵单元）的情况。
"""

def my_bisect_left(arr, key, lo, hi):
    """
    手动实现bisect_left：在arr[lo..hi)中找第一个>=key的位置
    """
    left = lo
    right = hi
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left

def solution():
    n = int(input())
    nums = list(map(int,input().split()))

    # 计算前缀和数组
    pre_sum = [0] * (n+1)
    for i in range(1,n+1):
        pre_sum[i] = pre_sum[i-1] + nums[i-1]

    sum_total = pre_sum[-1] # 上界
    target = sum_total / 7
    min_cost = sum_total # 初始值为s = 0的情况

    # 遍历每个右边界，二分查找最优左边界
    for r in range(1,n+1):
        key = pre_sum[r] - target
        # 在pre_sum[0..r-1]中查找最接近key的位置
        pos = my_bisect_left(pre_sum,key,0,r)

        # 检查pos位置的候选值
        if pos<r:
            s = pre_sum[r] - pre_sum[pos]
            current_cost = max(sum_total - s, 6*s)
            if current_cost < min_cost:
                min_cost = current_cost
        # 检查pos-1位置的候选值
        if pos>0:
            s = pre_sum[r] - pre_sum[pos-1]
            current_cost = max(sum_total - s, 6*s)
            if current_cost < min_cost:
                min_cost = current_cost
    print(min_cost)


"""
1. 指针移动的依据完全错误
    滑动窗口的核心是利用「sum 与 target 的大小关系」来移动指针（因为 nums[i]>0，sum 具有单调性）：
        若 sum_l_r < target：应右移 r（增大 sum，使其更接近 target）。
        若 sum_l_r > target：应右移 l（减小 sum，使其更接近 target）。
    但你的代码是用「current_cost 是否比 min_cost 小」来决定移动 r 还是 l，这与滑动窗口的单调性逻辑完全脱节，会直接错过大量可能的最优窗口。
2. 窗口有效性失控
    你的代码没有保证 l <= r，当 l > r 时，sum_l_r 会变成 0（无效窗口），直接跳过大量本应检查的区间。
"""
def solution2():
    """滑动窗口解决，因为本题也是连续的字串"""
    n = int(input())
    nums = list(map(int,input().split()))
    pre_sum = [0] * (n+1)
    for i in range(1,n+1):
        pre_sum[i] = pre_sum[i-1] + nums[i-1]
    total_sum = pre_sum[-1]
    l = 0
    r = 0
    min_cost = total_sum

    while l<n and r<n:
        # 计算l到r区间的总和
        sum_l_r = pre_sum[r+1] - pre_sum[l]
        current_cost = max(total_sum - sum_l_r, 6*sum_l_r)
        if current_cost < min_cost:
            min_cost = current_cost
            r += 1
        else:
            l += 1
    print(min_cost)


def solution2_correct():
    n = int(input())
    nums = list(map(int, input().split()))
    total_sum = sum(nums)
    target = total_sum / 7
    min_cost = total_sum  # 初始值为s=0的情况

    current_sum = 0
    left = 0

    for right in range(n):
        # 右指针右移，扩大窗口
        current_sum += nums[right]

        # 【关键】无论current_cost是否变小，都要先计算并更新min_cost
        current_cost = max(total_sum - current_sum, 6 * current_sum)
        if current_cost < min_cost:
            min_cost = current_cost

        # 【关键】根据sum与target的关系移动左指针，而非current_cost
        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1
            # 缩小窗口后再次计算并更新
            current_cost = max(total_sum - current_sum, 6 * current_sum)
            if current_cost < min_cost:
                min_cost = current_cost

    print(min_cost)


if __name__ == '__main__':
    #solution()
    #solution2()
    solution2_correct()