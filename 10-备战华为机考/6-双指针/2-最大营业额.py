"""
有条件下的最大连续和
"""
import sys


def solution():
    a = list(map(int,sys.stdin.readline().split()))
    n,m = a[0],a[1]
    nums = []
    for i in range(n):
        b = list(map(int,sys.stdin.readline().split()))
        nums.append(b)
    # 初始化
    cur_m = 0 #已占用人力
    cur_sum = 0
    res = 0
    left = None
    right = None
    for i in range(n):
        if nums[i][1] <= m - cur_m:
            if left is None or right is None: # 寻找符合条件的起始位置
                left = i
                right = i
                cur_sum = nums[i][0]
                res = max(res,cur_sum)
                cur_m = nums[i][1]
            else:
                right = i
                cur_sum += nums[i][0]
                cur_m += nums[i][1]
                res = max(res,cur_sum)
        elif nums[i][1] > m-cur_m and nums[i][1]<=m:
            for j in range(left,i+1):
                if cur_m - nums[j][1] + nums[i][1] <=m:
                    left = j+1
                    right = i
                    cur_m = cur_m - nums[j][1] + nums[i][1]
                    cur_sum = cur_sum - nums[j][0] + nums[i][0]
                    res = max(res,cur_sum)
                    break
                else:
                    left += 1
                    cur_m = cur_m - nums[j][1]
                    cur_sum = cur_sum - nums[j][0]
        else:
            cur_sum = 0
            cur_m = 0
            left = None
            right = None
    print(res)


if __name__ == '__main__':
    solution()