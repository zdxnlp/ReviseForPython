import sys

def solution():
    l = list(map(int,input().split()))
    m,n = l[0],l[1]
    for i in range(m):
        line = list(map(int,input().split()))

    sum_food = 0
    for i in range(m):
        for j in range(n):
                sum_food += 1
            else:


def main():
    input_data = sys.stdin.read().split()
    ptr = 0
    m = int(input_data[ptr])
    ptr += 1
    n = int(input_data[ptr])
    ptr += 1

    grid = []

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

    def dfs(x, y, collected):
        remaining = 0
        for (fx, fy) in foods:
            if not visited[fx][fy]:
                remaining += 1
        if collected + remaining < food_total:
            return
        if (x, y) == end and collected == food_total:
            return
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 3 and not visited[nx][ny]:
                visited[nx][ny] = True
                path.append((nx, ny))
                new_collected = collected + 1 if grid[nx][ny] == 2 else collected
                dfs(nx, ny, new_collected)
                path.pop()
                visited[nx][ny] = False

    path.append(start)
    visited[start[0]][start[1]] = True
    dfs(start[0], start[1], 0)

            print(x, y)
    else:
        print("null")


if __name__ == '__main__':
    solution()