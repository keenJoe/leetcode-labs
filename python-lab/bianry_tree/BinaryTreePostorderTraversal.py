# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs_postorder(root, res)
        return res
    
    def dfs_postorder(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if root:
            self.dfs_postorder(root.left, res)
            self.dfs_postorder(root.right, res)
            res.append(root.val)
        return res
    
    # 迭代
    def postorderTraversal_using_stack(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # todo

        return res
    
    # Morris遍历
    def postorderTraversal_using_morris(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # todo

        return res