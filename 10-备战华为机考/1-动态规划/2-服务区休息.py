import sys

"""
线性DP

任意连续M个服务区至少有一个服务区被休息 等价于 两次休息之间的间隔不能超过M个服务区

状态表示：dp[i]
    1.集合：在第i个服务区休息，且前i个服务区完全满足约束的所有方法
    2.属性：所有方法中，花费最小的
状态求解：
    1.上一次休息的位置j应该满足 i-j<=M 即j的范围为 max(0,i-M)<=j<=i-1
    2.dp[i] = cost[i] + min(dp[j] for j in [max(0,i-M),i-1])
初始化：
    dp[0] = 0
    
最终结果：
min(dp[i] for i in [max(1,N-M+1),N])
"""


def main():
    # 一次性读取所有输入，适配大数据量，避免IO超时
    input_data = sys.stdin.read().split()
    ptr = 0
    N = int(input_data[ptr])
    ptr += 1
    M = int(input_data[ptr])
    ptr += 1

    # 服务区费用数组，转换为1下标，方便dp计算
    cost = list(map(int, input_data[ptr:ptr + N]))
    cost = [0] + cost  # cost[1]~cost[N]对应第1~N个服务区的费用

    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[0] = 0  # 虚拟起点，初始花费为0

    for i in range(1, N + 1):
        # 上一次休息的左边界
        left = max(0, i - M)
        # 取范围内的最小dp值
        min_prev = min(dp[left:i])  # 切片左闭右开，正好覆盖left到i-1
        dp[i] = cost[i] + min_prev

    # 最终结果：最后M个服务区的dp最小值
    res_left = max(1, N - M + 1)
    min_total = min(dp[res_left:N + 1])
    print(min_total)


if __name__ == "__main__":
    main()