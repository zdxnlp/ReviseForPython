"""
1.预处理：遍历网格，记录起点、重点，统计所有食物的位置和总和
2.DFS+回溯搜索：
    a.状态记录：当前坐标、已收集的食物数据、已访问的格子标记、当前路径。
    b.终止条件：到达终点且收集所有食物，标记找到可行路径。
    c.递归逻辑：遍历上下左右4个方向，合法则标记访问、更新路径和收集数量，递归搜索；搜索失败则回溯(取消标记、回退路径)。
3.剪纸优化：若当前已收集的食物数+剩余未访问的食物数<总食物数，直接终止该分支的搜索，减少无效递归。
"""
import sys
sys.setrecursionlimit(10000)  # 增加递归深度，避免栈溢出

def solution():
    # 输入处理
    l = list(map(int,input().split()))
    m,n = l[0],l[1]
    grid = []
    for i in range(m):
        line = list(map(int,input().split()))
        grid.append(line)

    # 预处理
    start = None
    target = None
    food = []
    sum_food = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                start = (i,j)
            elif grid[i][j] == 1:
                target = (i,j)
            elif grid[i][j] == 2:
                food.append((i,j))
                sum_food += 1
    direction = [(-1,0),(1,0),(0,-1),(0,1)] # 上下左右4个方向
    visited = [[False for i in range(n)] for j in range(m)] # 标记已访问的格子
    path = [] # 记录当前路径
    found = False # 标记是否找到可行路径

    def dfs(x,y,collected):
        nonlocal found
        # 剪枝1:已找到路径，直接终止所有递归
        if found:
            return
        # 剪枝2:剩余可收集的食物不足，无法完成目标，直接返回
        remaining = 0
        for (fx,fy) in food:
            if not visited[fx][fy]:
                remaining += 1
        if collected + remaining < sum_food:
            return

        # 终止条件
        if (x,y) == target and collected == sum_food:
            found = True
            return

        # 遍历4个方向
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            # 检查边界、障碍、是否已访问
            if 0<=nx<m and 0<=ny<n and grid[nx][ny] != 3 and not visited[nx][ny]:
                # 标记访问、更新路径
                visited[nx][ny] = True
                path.append((nx,ny))
                # 更新收集的食物数量
                new_collected = collected + 1 if grid[nx][ny] == 2 else collected
                # 递归搜索
                dfs(nx,ny,new_collected)
                if found:
                    return
                # 回溯
                path.pop()
                visited[nx][ny] = False

    path.append(start)
    visited[start[0]][start[1]] = True
    dfs(start[0],start[1],0)

    if found:
        for (x,y) in path:
            print(x,y)
    else:
        print('null')


def main():
    input_data = sys.stdin.read().split()
    ptr = 0
    m = int(input_data[ptr])
    ptr += 1
    n = int(input_data[ptr])
    ptr += 1

    grid = []
    start = None
    end = None
    foods = []

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
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    path = []
    all_paths = []  # 【新增】用于存储所有有效路径

    def dfs(x, y, collected):
        nonlocal all_paths

        # 剪枝：剩余可收集食物不足，直接返回
        remaining = 0
        for (fx, fy) in foods:
            if not visited[fx][fy]:
                remaining += 1
        if collected + remaining < food_total:
            return

        # 【修改】终止条件：到达终点且收集完所有食物，保存路径副本
        if (x, y) == end and collected == food_total:
            all_paths.append(path.copy())  # 必须存copy，否则回溯会清空path
            return

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 3 and not visited[nx][ny]:
                visited[nx][ny] = True
                path.append((nx, ny))
                new_collected = collected + 1 if grid[nx][ny] == 2 else collected

                dfs(nx, ny, new_collected)

                # 【移除】不再提前返回，继续搜索其他路径
                path.pop()
                visited[nx][ny] = False

    # 初始化
    path.append(start)
    visited[start[0]][start[1]] = True
    dfs(start[0], start[1], 0)

    # 【修改】输出所有路径
    if all_paths:
        print(f"找到 {len(all_paths)} 条有效路径：")
        for idx, p in enumerate(all_paths, 1):
            print(f"\n路径 {idx}:")
            for (x, y) in p:
                print(x, y)
    else:
        print("null")


if __name__ == '__main__':
    solution()