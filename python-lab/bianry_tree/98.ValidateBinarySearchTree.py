# 98. Validate Binary Search Tree

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归。
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs_is_valid_bst(root, float('-inf'), float('inf'))
    
    def dfs_is_valid_bst(self, cur: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if not cur:
            return True
        
        return (cur.val > min_val 
                and cur.val < max_val 
                and self.dfs_is_valid_bst(cur.left, min_val, cur.val)
                and self.dfs_is_valid_bst(cur.right, cur.val, max_val))
    

    # 迭代。如果用迭代，那么其实就是中序遍历，最后判断结果是否是递增的。
    def isValidBST_iter(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = []
        stack.append(root)
        pre = float('-inf')
        while stack:
            node = stack.pop()
            if node:
                if not node.left:
                    if pre >= node.val:
                        return False
                    pre = node.val
                    stack.append(node.right)
                else:
                    stack.append(node)
                    stack.append(node.left)
                    node.left = None

        return True
    
    def inorderTraversal_using_stack_2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = []
        pre = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right

        return True
