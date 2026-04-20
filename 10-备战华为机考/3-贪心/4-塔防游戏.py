"""
1.i时刻初，检查i+1时刻初谁离得更近。i时刻初击杀i+1时刻初最近的那个
2.击杀完成后要检查是否有敌人在i初到i+1初之间就到了城堡

敌人完全消灭 敌人进入城堡 游戏结束
"""

import sys


def main():
    n = int(input())
    dist = list(map(int, input().split()))
    speed = list(map(int, input().split()))

    # 计算每个敌人的到达时间
    arrive_time = []
    for d, s in zip(dist, speed):
        arrive_time.append(d / s)

    # 按到达时间从小到大排序
    arrive_time.sort()

    # 遍历计算最大击杀数
    max_kill = 0
    for i in range(n):
        if arrive_time[i] > i:
            max_kill += 1
        else:
            # 有敌人到达，游戏结束
            break

    print(max_kill)


if __name__ == "__main__":
    main()
