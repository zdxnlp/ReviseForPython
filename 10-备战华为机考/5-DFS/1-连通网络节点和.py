def main():
    import sys
    from collections import deque

    # 步骤1：读取输入并初始化数据结构
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    ptr = 0

    # 读取节点数n
    n = int(input_lines[ptr])
    ptr += 1

    # 存储节点名称→权重的映射
    node_weight = {}
    for _ in range(n):
        name, weight = input_lines[ptr].split()
        node_weight[name] = int(weight)
        ptr += 1

    # 读取连接关系数m
    m = int(input_lines[ptr])
    ptr += 1

    # 构建邻接表（无向图）
    adj = {name: [] for name in node_weight.keys()}
    for _ in range(m):
        parts = input_lines[ptr].split()
        ptr += 1
        # 处理"0"的情况（无连接）
        if parts[0] == '0' or len(parts) < 2:
            continue
        u, v = parts[0], parts[1]
        adj[u].append(v)
        adj[v].append(u)

    # 步骤2：遍历所有连通分量，计算每个分量的信息
    visited = set()  # 标记已访问的节点
    max_total_weight = -1  # 最大的网络权重和
    max_node_in_best_network = ""  # 权重最大网络中权重最大的节点

    for node in node_weight.keys():
        if node not in visited:
            # BFS遍历当前连通分量
            q = deque()
            q.append(node)
            visited.add(node)
            current_total = 0  # 当前分量的总权重
            current_max_weight = -1  # 当前分量内最大权重
            current_max_node = ""  # 当前分量内权重最大的节点

            while q:
                curr = q.popleft()
                # 更新当前分量的总权重
                curr_w = node_weight[curr]
                current_total += curr_w
                # 更新当前分量内权重最大的节点
                if curr_w > current_max_weight:
                    current_max_weight = curr_w
                    current_max_node = curr

                # 遍历邻接节点
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

            # 步骤3：比较当前分量和已找到的最大分量
            if current_total > max_total_weight:
                max_total_weight = current_total
                max_node_in_best_network = current_max_node

    # 输出结果
    print(max_node_in_best_network, max_total_weight)

if __name__ == "__main__":
    main()