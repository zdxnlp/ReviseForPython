from ast import List
from collections import deque

from sympy import preorder_traversal


class TreeNode:
    """二叉树的节点"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left # 左孩子
        self.right = right # 右孩子

class Solution:
    def __init__(self, root:TreeNode):
        self.root = root

    def preorderTraversal(self, root: TreeNode):
        pre = []
        def dfs(root: TreeNode):
            if root:
                pre.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return pre

    def inorderTraversal(self, root: TreeNode):
        pre = []
        def dfs(root: TreeNode):
            if root:
                dfs(root.left)
                pre.append(root.val)
                dfs(root.right)
        dfs(root)
        return pre

    def postorderTraversal(self, root: TreeNode):
        pre = []
        def dfs(root: TreeNode):
            if root:
                dfs(root.left)
                dfs(root.right)
                pre.append(root.val)
        dfs(root)
        return pre

    def levelOrder(self, root: TreeNode):
        if not root:
            return
        res = []
        queue = deque([root]) # 辅助队列
        while queue:
            level_size = len(queue) # 当前层的节点数
            current_level = [] # 存储当前层的节点值
            for _ in range(level_size):
                node = queue.popleft() # 队首元素出队
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(current_level)
        return res

class IterationSolution:
    def __init__(self, root:TreeNode):
        self.root = root

    def preOrder(self, root: TreeNode):
        if not root:
            return []
        stack = [root] # 用栈存储节点
        res = []
        while stack:
            node = stack.pop() # 弹出栈顶节点
            res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return res

    def inOrder(self, root: TreeNode):
        """
        1.一直向右边遍历，直到找到最右边的节点（他一定没有左孩子，可能有右孩子）
        2.找到最右边的孩子就弹出栈，出栈的时候检查是否有左孩子，有左孩子就跳转到1继续
        3.重复上述步骤直到栈空
        """
        if not root:
            return []
        stack = []
        res = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right
        return res

    def postOrder(self, root: TreeNode):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            # 先压左子节点，再压右子节点（保证弹出时先处理右子节点）
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        # 反转结果得到后序遍历
        return result[::-1]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution(root).preorderTraversal(root))
    print(Solution(root).inorderTraversal(root))
    print(Solution(root).postorderTraversal(root))
    print(Solution(root).levelOrder(root))

    print(IterationSolution(root).preOrder(root))
    print(IterationSolution(root).inOrder(root))
    print(IterationSolution(root).postOrder(root))