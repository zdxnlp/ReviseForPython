def solve():
    n = int(input())

    # 特判：只有一个节点
    if n == 1:
        init_val = int(input())
        goal_val = int(input())
        print(0 if init_val == goal_val else 1)
        return

    # 建图
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 读取初始值和目标值
    init_vals = [0] + list(map(int, input().split()))
    goal_vals = [0] + list(map(int, input().split()))

    operations = 0

    def dfs(node, parent, flip_even, flip_odd, depth):
        """
        node: 当前节点
        parent: 父节点
        flip_even: 偶数深度祖先的操作次数
        flip_odd: 奇数深度祖先的操作次数
        depth: 当前深度
        """
        nonlocal operations

        # 当前节点受到的翻转次数（偶数距离的祖先操作会影响当前节点）
        if depth % 2 == 0:
            current_flip = flip_even
        else:
            current_flip = flip_odd

        # 计算当前节点的实际值
        current_val = (init_vals[node] + current_flip) % 2

        # 判断是否需要操作
        need_flip = 0
        if current_val != goal_vals[node]:
            need_flip = 1
            operations += 1

        # 递归处理子节点
        for child in graph[node]:
            if child != parent:
                if depth % 2 == 0:
                    # 当前是偶数深度，子节点是奇数深度
                    dfs(child, node, flip_even + need_flip, flip_odd, depth + 1)
                else:
                    # 当前是奇数深度，子节点是偶数深度
                    dfs(child, node, flip_even, flip_odd + need_flip, depth + 1)

    # 从根节点1开始DFS，深度为0
    dfs(1, -1, 0, 0, 0)
    print(operations)


if __name__ == '__main__':
    solve()