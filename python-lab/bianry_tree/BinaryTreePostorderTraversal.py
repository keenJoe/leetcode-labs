# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs_postorder(root, res)
        return res
    
    def dfs_postorder(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if root:
            self.dfs_postorder(root.left, res)
            self.dfs_postorder(root.right, res)
            res.append(root.val)
        return res
    
    # 迭代
    def postorderTraversal_using_stack(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        stack = []
        stack.append(root)
        while stack:
            # 获取栈顶元素
            node = stack[-1]
            if not node.left and not node.right:
                res.append(node.val)
                stack.pop()
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                if node.left:
                    stack.append(node.left)
                    node.left = None

        return res
    
    # Morris遍历
    def postorderTraversal_using_morris(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        cur = root
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    # 添加反转后的路径
                    self.addPath(cur.left, res)
                    cur = cur.right
        
        # 最后添加整个右边界
        self.addPath(root, res)
        return res
    
    def addPath(self, node: TreeNode, res: List[int]):
        tail = self.reverseNode(node)
        cur = tail
        while cur:
            res.append(cur.val)
            cur = cur.right
        self.reverseNode(tail)  # 恢复原来的顺序
    
    def reverseNode(self, node: TreeNode) -> TreeNode:
        pre = None
        cur = node
        while cur:
            next = cur.right
            cur.right = pre
            pre = cur
            cur = next
        return pre