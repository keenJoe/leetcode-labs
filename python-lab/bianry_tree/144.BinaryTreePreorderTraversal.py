# 144. Binary Tree Preorder Traversal

"""
前序遍历：根节点 -> 左子树 -> 右子树
1、递归
2、使用栈进行迭代
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs_preorder(root, res)
        return res

    def dfs_preorder(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if root:
            res.append(root.val)
            self.dfs_preorder(root.left, res)
            self.dfs_preorder(root.right, res)
        return res

    # 迭代，使用栈1
    def preorderTraversal_using_stack(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        while stack or root:
            # 先遍历左子树，直到左子树为空
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left

            # 左子树为空，则弹出栈顶元素，访问右子树
            root = stack.pop()
            root = root.right
        return res
    

    # 迭代，使用栈2
    def preorderTraversal_using_stack(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res


    # 迭代，morris
    # Morris不再使用栈，那么当根节点的左右节点都为空，需要回到根节点，然后开始遍历右节点。但是因为当前节点的左节点不为空，会继续遍历左节点。这样就会形成一个环。
    # 那么需要利用空闲节点。
    # 将当前节点的左子树的最右节点指向当前节点。这样做的目的是：当回到根节点时，可以知道当前节点已经遍历过左子树。这样就解决了环的问题。
    def preorderTraversal_morris(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                
                if not cur.right:
                    cur.right = root
                    res.append(root.val)
                    root = root.left
                else:
                    cur.right = None
                    root = root.right

        return res
        
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    print(s.preorderTraversal(root))

