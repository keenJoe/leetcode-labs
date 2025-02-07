# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1. 递归
    def minDepth_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        min_depth = float('inf')
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        return min_depth + 1
    
    # 2. 递归，这个方法比上一个方法更简洁且更加高效
    def minDepth_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left and not root.right:
            return self.minDepth(root.left) + 1
        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    

    # 3. 迭代，使用广度优先搜索，当找到一个叶子节点时，直接返回当前的深度。
    # 按照自己之前的思路，就是前序遍历，然后记录一个最小深度，但是这个方法需要遍历所有的节点，所以效率不高。
    def minDepth_iter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0
