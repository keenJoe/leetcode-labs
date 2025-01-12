# 107. Binary Tree Level Order Traversal II

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归。
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs_level_order_bottom(root, 0, res)
        return res
    
    def dfs_level_order_bottom(self, root: Optional[TreeNode], level: int, res: List[List[int]]):
        if not root:
            return
        
        if len(res) == level:
            res.insert(0, [])  # 在开头插入新层
        res[-(level+1)].append(root.val)  # 从末尾反向访问对应层
        self.dfs_level_order_bottom(root.left, level + 1, res)
        self.dfs_level_order_bottom(root.right, level + 1, res)


    # 迭代。使用队列。
    def levelOrderBottom_iter(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            level_res = []
            for _ in range(size):
                node = queue.pop(0)
                level_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.insert(0, level_res)  # 在开头插入新层
        return res
