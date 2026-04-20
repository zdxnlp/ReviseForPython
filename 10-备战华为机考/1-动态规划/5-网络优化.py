"""
题目要求移除最少设备，使得剩余树的所有叶子节点到根的距离相同。
等价于
找到一个目标深度D，使得保留的树的所有叶子深度都是D，且保留的节点数最多

最少移除数 = 总结点数 - 最大保留节点数
"""
from collections import deque

"""
1.构建有根树：输入是无向边，以1为根，使用BFS遍历树，记录每个节点的
    子节点 深度， 同时计算树的最大深度 max_depth

2.预计算后续遍历序列：后序遍历保证处理父节点前，所有子节点都已处理，为后续动态
    规划做准备，避免递归开销
    
3.枚举目标深度D：D的范围是1到max_depth（根的深度为0）
    A.对每个D，按后续顺序计算每个节点的最大保留数keep[u]:
        a.若节点u的深度等于D：keep[u] = 1（u必须是叶子，仅保留自己）
        b.若节点u的深度小于D：累加所有子节点的keep[v]（仅保留能满足D的子树），
            若总和>0，keep[u] = 1 + 总和(加上自己)；否则keep[u] = 0（无法满足D）

4.计算结果：找到所有D中根节点的最大keep[1]，最终答案为n-max_keep
"""

def solution():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # BFS构建以1为根的有根树，记录子节点、深度
    children = [[] for _ in range(n+1)]
    depth = [0] * (n+1)
    parent = [0] * (n+1)
    q = deque([1])
    parent[1] = -1
    max_depth = 0

    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                if depth[v] > max_depth:
                    max_depth = depth[v]
                children[u].append(v)
                q.append(v)

    # 预计算后序遍历序列（迭代实现，避免递归栈溢出）
    post_order = []
    stack = [(1,False)]
    while stack:
        node,visited = stack.pop()
        if visited:
            post_order.append(node)
            continue
        stack.append((node,True))
        # 子节点逆序入栈，保证遍历顺序正确
        for child in reversed(children[node]):
            stack.append((child,False))

    max_keep = 0 # 记录最多保留的节点数
    # 枚举所有可能的目标深度D
    for D in range(1,max_depth+1):
        keep = [0] * (n+1)
        for u in post_order:
            if depth[u] == D:
                keep[u] = 1
            else:
                # 累加所有子节点的可保留数
                sum_keep = 0
                for v in children[u]:
                    sum_keep += keep[v]
                # 有合法子树则保留当前节点，否则不可达
                keep[u] = 1 + sum_keep if sum_keep > 0 else 0
        # 更新最大保留数
        if keep[1] > max_keep:
            max_keep = keep[1]

    print(n-max_keep)



if __name__ == '__main__':
    solution()