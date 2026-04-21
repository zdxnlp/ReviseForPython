"""
核心是找到连续x天的区间，使得区间内的金币总和最大。
每个月的第k天获得k个金币，日历每年循环，且x不超过一年的总天数。

最优的连续x天窗口，一定结束在某个月的月末：
    原因：每个月内的金币随天数递增，窗口向右移动时，新增的月末金币收益会超过窗口左侧移除的金币收益，因此每个月的最大收益窗口必然结束在月末
    “穷举所有可能的起始天”->“穷举所有月份的月末”
"""
import sys


def solution():
    res = 0
    line1 = list(map(int, input().split()))
    n,x = line1[0],line1[1]
    line2 = list(map(int, input().split()))
    month = line2
    for i in range(n):
        month.append(line2[i])
    left = 0
    right = 0
    pre_sum = [0] * (2*n+1) # 这样设计的时候区间[left,right]的和是 days =  pre_sum[right+1] - pre_sum[left]
    current_sum = 0
    for i in range(0,2*n):
        current_sum += month[i]
        pre_sum[i+1] = current_sum

    while right < 2*n and left <= right:
        days = pre_sum[right+1] - pre_sum[left]
        if days < x:
            right += 1
            continue
        else:
            pos = right
            count = x
            current = 0
            while pos>=left and count>=1:
                current_day = month[pos]
                while current_day >= 1:
                    if count < 1:
                        break
                    current += current_day
                    current_day -= 1
                    count -= 1
                pos -= 1
            left += 1
            res = max(res,current)
    print(res)

if __name__ == '__main__':
    solution()
