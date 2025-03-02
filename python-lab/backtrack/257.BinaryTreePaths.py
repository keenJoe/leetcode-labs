# 257. Binary Tree Paths

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        
        def backtrack(root):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                res.append('->'.join(map(str, path)))
                return
            if root.left:
                backtrack(root.left)
                path.pop()
            if root.right:
                backtrack(root.right)
                path.pop()
        
        backtrack(root)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.binaryTreePaths(TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3))))
        