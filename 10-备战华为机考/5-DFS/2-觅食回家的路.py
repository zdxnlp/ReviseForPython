import sys

def solution():
    l = list(map(int,input().split()))
    m,n = l[0],l[1]
    value_map = []
    for i in range(m):
        line = list(map(int,input().split()))
        value_map.append(line)

    begin_pos = []
    target_pos = []
    food_pos = []
    forbidden_pos = []
    sum_food = 0
    for i in range(m):
        for j in range(n):
            if value_map[i][j] == 0:
                begin_pos.append([i,j])
            elif value_map[i][j] == 1:
                target_pos.append([i,j])
            elif value_map[i][j] == 2:
                food_pos.append([i,j])
                sum_food += 1
            else:
                forbidden_pos.append([i,j])




sys.setrecursionlimit(10000)  # 增加递归深度，避免栈溢出

def main():
    # 读取输入，适配ACM标准输入
    input_data = sys.stdin.read().split()
    ptr = 0
    m = int(input_data[ptr])
    ptr += 1
    n = int(input_data[ptr])
    ptr += 1

    grid = []
    start = None  # 起点(0)坐标
    end = None  # 终点(1)坐标
    foods = []  # 所有食物(2)的坐标列表

    # 解析网格
    for i in range(m):
        row = list(map(int, input_data[ptr:ptr + n]))
        ptr += n
        grid.append(row)
        for j in range(n):
            if row[j] == 0:
                start = (i, j)
            elif row[j] == 1:
                end = (i, j)
            elif row[j] == 2:
                foods.append((i, j))

    food_total = len(foods)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右4个方向
    visited = [[False for _ in range(n)] for _ in range(m)]  # 标记已访问的格子
    path = []  # 记录当前路径
    found = False  # 标记是否找到可行路径

    def dfs(x, y, collected):
        nonlocal found
        # 剪枝1：已找到路径，直接终止所有递归
        if found:
            return
        # 剪枝2：剩余可收集的食物不足，无法完成目标，直接返回
        remaining = 0
        for (fx, fy) in foods:
            if not visited[fx][fy]:
                remaining += 1
        if collected + remaining < food_total:
            return
        # 终止条件：到达终点，且收集了所有食物
        if (x, y) == end and collected == food_total:
            found = True
            return
        # 遍历4个方向
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            # 检查边界、障碍、是否已访问
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 3 and not visited[nx][ny]:
                # 标记访问，更新路径
                visited[nx][ny] = True
                path.append((nx, ny))
                # 更新收集的食物数量
                new_collected = collected + 1 if grid[nx][ny] == 2 else collected
                # 递归搜索
                dfs(nx, ny, new_collected)
                if found:
                    return
                # 回溯：恢复状态
                path.pop()
                visited[nx][ny] = False

    # 初始化：起点加入路径，标记为已访问
    path.append(start)
    visited[start[0]][start[1]] = True
    # 启动DFS，初始收集食物数为0（起点不是食物）
    dfs(start[0], start[1], 0)

    # 输出结果
    if found:
        # 输出路径，每行一个坐标，格式为 x y
        for (x, y) in path:
            print(x, y)
    else:
        print("null")


if __name__ == "__main__":
    main()


if __name__ == '__main__':
    solution()