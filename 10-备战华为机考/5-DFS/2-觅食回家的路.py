import sys
def solution():
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    ptr = 0
    m,n = list(map(int,input_lines[ptr].split()))
    grid = []
    ptr += 1
    for _ in range(m):
        grid.append(list(map(int, input_lines[ptr].split())))
        ptr += 1

    start = None
    target = None
    food = [] # 食物的位置
    total = 0 # 总的食物个数
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 每个节点的移动方向

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                target = (i, j) # 目标位置
            elif grid[i][j] == 2:
                food.append((i, j))
                total = total + 1
            elif grid[i][j] == 0:
                start = (i, j) # 起始位置

    path = []
    all_path = []

    visited = [[False] * n for _ in range(m)]

    def dfs(x,y,collected):
        nonlocal all_path
        remaining = 0
        for (fx,fy) in food:
            if not visited[fx][fy]:
                remaining += 1
        if collected + remaining < total:
            return

        if (x,y) == target and collected == total:
            all_path.append(path.copy())
            return

        for dx,dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 3 and not visited[nx][ny]:
                visited[nx][ny] = True
                path.append((nx,ny))
                new_collected = collected + 1 if grid[nx][ny] == 2 else collected

                dfs(nx,ny,new_collected)

                path.pop()
                visited[nx][ny] = False

    path.append(start)
    visited[start[0]][start[1]] = True
    dfs(start[0],start[1],0)

    print(len(all_path))

if __name__ == '__main__':
    solution()