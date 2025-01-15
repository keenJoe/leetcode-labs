# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归。
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs_depth(root)
    
    def dfs_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.dfs_depth(root.left), self.dfs_depth(root.right)) + 1
    

    # 迭代。使用栈。
    # 使用栈来模拟递归的过程，通过栈来保存当前节点和其深度。
    # 在这一瞬间，真的爱上python了。
    def maxDepth_iter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = []
        # 初始化栈，将根节点和其深度（1）压入栈中。
        # amazing！
        stack.append((root, 1))
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth

    # 迭代。使用队列。其实就是层序遍历。
    # 层序遍历的本质就是广度优先搜索（BFS），没完成一层，深度就加1。
    def maxDepth_iter_queue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = []
        queue.append(root)
        max_depth = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_depth += 1
        return max_depth
