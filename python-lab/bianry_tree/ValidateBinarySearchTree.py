# 98. Validate Binary Search Tree

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs_is_valid_bst(root, float('-inf'), float('inf'))
    
    def dfs_is_valid_bst(self, cur: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if not cur:
            return True
        
        return (cur.val > min_val 
                and cur.val < max_val 
                and self.dfs_is_valid_bst(cur.left, min_val, cur.val)
                and self.dfs_is_valid_bst(cur.right, cur.val, max_val))
