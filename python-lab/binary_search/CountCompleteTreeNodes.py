# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        height = 0
        node  = root
        while node.left:
            height += 1
            node = node.left

        left, right = 0, (1 << height) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.exists(root, height, mid):
                left = mid + 1
            else:
                right = mid - 1

        return (1 << height) - 1 + left
    
    def exists(self, root: TreeNode, height: int, mid: int) -> bool:
        left, right = 0, (1 << height) - 1
        for _ in range(height):
            mid = left + (right - left) // 2
            if mid & 1:
                root = root.right
            else:
                root = root.left
        return root is not None


if __name__ == "__main__":
    solution = Solution()
    print(solution.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))
    print(solution.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))