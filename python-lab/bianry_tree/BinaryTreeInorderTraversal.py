# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 中序遍历：左子树 -> 根节点 -> 右子树
class Solution:
    # 递归
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs_inorder(root, res)
        return res

    def dfs_inorder(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if root:
            self.dfs_inorder(root.left, res)
            res.append(root.val)
            self.dfs_inorder(root.right, res)
        return res

    # 迭代
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pass
