# 100. Same Tree

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归。
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

    # 迭代
    def isSameTree_iter(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        p_stack = [p]
        q_stack = [q]
        
        while p_stack and q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()
            if p_node.val != q_node.val:
                return False
            
            if p_node.left and q_node.left:
                p_stack.append(p_node.left)
                q_stack.append(q_node.left)
            elif p_node.left or q_node.left:
                return False
            
            if p_node.right and q_node.right:
                p_stack.append(p_node.right)
                q_stack.append(q_node.right)
            elif p_node.right or q_node.right:
                return False
            
        return True
