# 113. Path Sum II

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(root, targetSum):
            if not root:
                return
            
            path.append(root.val)
            targetSum -= root.val

            if not root.left and not root.right:
                if targetSum == 0:
                    res.append(path[:])
                return
            
            if root.left:
                backtrack(root.left, targetSum)
                path.pop()
            if root.right:
                backtrack(root.right, targetSum)
                path.pop()
                
        backtrack(root, targetSum)
        return res

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    targetSum = 22
    print(s.pathSum(root, targetSum))