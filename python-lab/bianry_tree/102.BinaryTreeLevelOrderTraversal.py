# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 迭代。使用队列。
    # 如果当前节点的左右节点不为空，则将左右节点入队。
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            res.append(level_res)
        return res
    
    # 递归。
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        self.dfs_level_order(root, 0, res)
        return res
    
    def dfs_level_order(self, root: Optional[TreeNode], level: int, res: List[List[int]]):
        if not root:
            return
        
        if len(res) == level:
            res.append([])
        # 将当前节点的值添加到对应层的列表中
        res[level].append(root.val)
        self.dfs_level_order(root.left, level + 1, res)
        self.dfs_level_order(root.right, level + 1, res)
