"""
1.角色在矩阵中只能向右或向下移动（从二维的角度看）从自己的角度就是向前向右
2.只能从右侧出去
3.相邻节点高度差大于1不可达
4.经过[i][j]会消耗map[i][j]的体力
5.求解最小的体力值
"""
from cv2.typing import map_int_and_double

"""
1.状态表示：dp[i][j]:表示角色到达(i,j)的所有路径中，所需的最小体力
2.状态计算：
    a.从左来：
        from_left = dp[i][j-1] + map[i][j] if abs(map[i][j] - map[i][j-1])<=1 else inf
    b.从上来：
        from_up = dp[i-1][j] + map[i][j] if abs(map[i][j] - map[i-1][j])<=1 else inf
    
    dp[i][j] = min(from_left,from_up)
"""

def solution():
    k = int(input())
    value_map = []
    for i in range(k):
        value_map.append(list(map(int,input().split())))
    inf = 1
    for i in range(k):
        for j in range(k):
            inf += value_map[i][j]
    dp = [[0 for _ in range(k)] for _ in range(k)]
    for i in range(0,k):
        for j in range(0,k):
            if i==0 and j==0:
                dp[i][j] = value_map[i][j]
            elif i==0 and j!=0:
                dp[i][j] = dp[i][j-1] + value_map[i][j] if abs(value_map[i][j] - value_map[i][j-1])<=1 else inf
            elif j==0 and i!=0:
                dp[i][j] = dp[i-1][j] + value_map[i][j] if abs(value_map[i][j] - value_map[i-1][j])<=1 else inf
            else:
                from_left = dp[i][j - 1] + value_map[i][j] if abs(value_map[i][j] - value_map[i][j - 1]) <= 1 else inf
                from_up = dp[i - 1][j] + value_map[i][j] if abs(value_map[i][j] - value_map[i - 1][j]) <= 1 else inf
                dp[i][j] = min(from_left,from_up)
    min_cost = dp[0][k-1]
    for i in range(1,k):
        min_cost = min(min_cost,dp[i][k-1])
    if min_cost==inf:
        print(-1)
    else:
        print(min_cost)

import sys

def main():
    # 常量定义：足够大的不可达值（远大于最大可能路径和）
    INF = 10 ** 9
    # 题目约束的参数范围
    MAX_K = 100
    MIN_HEIGHT = 0
    MAX_HEIGHT = 10

    # 一次性读取所有输入，提升鲁棒性，避免多次IO异常
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    ptr = 0

    # ====================== 1. 参数合法性检查 ======================
    # 检查k的合法性
    try:
        k = int(input_lines[ptr])
        ptr += 1
    except (ValueError, IndexError):
        print(-2)
        return
    if k < 1 or k > MAX_K:
        print(-2)
        return

    # 读取并检查矩阵合法性
    grid = []
    for _ in range(k):
        try:
            row = list(map(int, input_lines[ptr].split()))
            ptr += 1
        except (ValueError, IndexError):
            print(-2)
            return
        # 检查每行元素数量是否为k
        if len(row) != k:
            print(-2)
            return
        # 检查每个元素的高度范围
        for num in row:
            if not (MIN_HEIGHT <= num <= MAX_HEIGHT):
                print(-2)
                return
        grid.append(row)

    # ====================== 2. DP数组初始化 ======================
    # dp[i][j] 表示到达(i,j)的最小体力消耗，初始化为不可达
    dp = [[INF] * k for _ in range(k)]
    # 起点初始化：进入起点即消耗对应体力
    dp[0][0] = grid[0][0]

    # ====================== 3. 状态转移 ======================
    for i in range(k):
        for j in range(k):
            # 起点已初始化，跳过
            if i == 0 and j == 0:
                continue
            # 候选路径集合
            candidates = []
            # 路径1：从上方(i-1,j)过来
            if i > 0:
                # 高度差符合要求，且上方可达
                if abs(grid[i][j] - grid[i-1][j]) <= 1 and dp[i-1][j] != INF:
                    candidates.append(dp[i-1][j] + grid[i][j])
            # 路径2：从左方(i,j-1)过来
            if j > 0:
                # 高度差符合要求，且左方可达
                if abs(grid[i][j] - grid[i][j-1]) <= 1 and dp[i][j-1] != INF:
                    candidates.append(dp[i][j-1] + grid[i][j])
            # 取最小消耗，无合法路径则保持INF
            if candidates:
                dp[i][j] = min(candidates)

    # ====================== 4. 结果计算 ======================
    # 终点是最后一列的任意行，取最小消耗
    min_cost = min(dp[i][k-1] for i in range(k))

    # 输出结果
    if min_cost == INF:
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    solution()
