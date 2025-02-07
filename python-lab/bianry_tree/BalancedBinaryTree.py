# 110. Balanced Binary Tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1. 递归，自顶向下，需要计算每一个节点的高度，然后判断是否平衡
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    

    # 2. 递归，自底向上，不需要计算每一个节点的高度，只需要判断是否平衡
    def isBalanced_2(self, root: Optional[TreeNode]) -> bool:
        return self.height_2(root) >= 0
    
    def height_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.height_2(root.left)
        right_height = self.height_2(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    

    # 3. 迭代，使用广度优先搜索，当找到一个不平衡的节点时，直接返回False。
    def isBalanced_iter(self, root: Optional[TreeNode]) -> bool:
        pass
