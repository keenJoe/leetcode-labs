# 114. Flatten Binary Tree to Linked List


'''
1、先序遍历
2、从根节点开始，但在移动到左节点之前，先保存好右节点，然后断开根节点和右节点之间的连接；
'''


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 迭代 + 右子树暂存
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            current = stack.pop()
            
            # 先压右子树，再压左子树（因为栈是后进先出）
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            
            # 连接前一个节点
            if prev:
                prev.left = None
                prev.right = current
            
            prev = current

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        # 先序遍历收集所有节点
        nodes = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            nodes.append(node)
            
            # 先压右，再压左
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        # 重构树
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        
        nodes[-1].left = None
        nodes[-1].right = None

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    solution.flatten(root)
    while root:
        print(root.val, end=" ")
        root = root.right