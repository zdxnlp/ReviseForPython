def solve():
    m = int(input())
    nums = list(map(int, input().split()))

    if m <= 1:
        print(0)
        return

    max_diff = 0
    i = 0

    while i < m:
        # 找到波峰区间的起点（跳过递减部分）
        while i < m - 1 and nums[i] > nums[i + 1]:
            i += 1

        if i >= m - 1:
            break

        # 记录区间起点
        start = i
        peak_min = nums[i]
        peak_max = nums[i]

        # 上升阶段：单调非递减
        while i < m - 1 and nums[i] <= nums[i + 1]:
            i += 1
            peak_max = max(peak_max, nums[i])

        # 记录峰顶位置
        peak_pos = i

        # 下降阶段：单调非递增
        while i < m - 1 and nums[i] >= nums[i + 1]:
            i += 1
            peak_min = min(peak_min, nums[i])
            peak_max = max(peak_max, nums[i])

        # 只有经历了上升和下降才是有效的波峰区间
        if peak_pos > start and i > peak_pos:
            max_diff = max(max_diff, peak_max - peak_min)
        # 只有上升没有下降，也算一个波峰区间
        elif peak_pos > start:
            max_diff = max(max_diff, peak_max - peak_min)

    print(max_diff)


if __name__ == '__main__':
    solve()


# ==================== 原代码错误分析 ====================
# 原代码存在以下问题：
#
# 1. 状态转换逻辑混乱：
#    - 使用 if 而不是 elif，导致多个条件可能同时执行
#    - 例如：nums[i] < nums[right] 和 nums[i] > nums[right] 后面都没有用 elif
#    - 这会导致状态转换不清晰，可能重复更新
#
# 2. 边界处理错误：
#    - 当 down=True 且遇到上升时，重置为 left=i-1, right=i-1
#    - 但此时应该从当前位置重新开始寻找波峰区间，而不是回退
#
# 3. 波峰区间定义不准确：
#    - 题目要求"先上升后下降"，但原代码允许只上升或只下降的情况
#    - 没有明确判断是否完成了完整的波峰（上升+下降）
#
# 4. 最小值更新错误：
#    - cur_min 应该在整个波峰区间内更新，但原代码只在下降阶段更新
#    - 上升阶段的起点可能是最小值，但没有正确维护
#
# 5. 相等情况处理不当：
#    - else 分支只是简单地 right = i，没有考虑相等时应该继续当前趋势
#    - 题目允许"单调非递减"和"单调非递增"，即允许相等
#
# 6. 区间重置时机错误：
#    - 当从下降转为上升时，应该结束当前波峰区间并开始新的搜索
#    - 但原代码的重置逻辑会丢失部分有效区间
#
# 正确思路：
# - 使用贪心+双指针
# - 明确三个阶段：跳过下降 → 上升 → 下降
# - 只有完成上升阶段的区间才是有效波峰区间
# - 每次找到一个波峰区间后，从下一个位置继续搜索