# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归。
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs_zigzag_level_order(root, 0, res)
        return res
    
    def dfs_zigzag_level_order(self, root: Optional[TreeNode], level: int, res: List[List[int]]):
        if not root:
            return 
        
        if len(res) == level:
            res.append([])
        if level % 2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)
        self.dfs_zigzag_level_order(root.left, level + 1, res)
        self.dfs_zigzag_level_order(root.right, level + 1, res)

    # 迭代。使用队列。
    def zigzagLevelOrder_iter(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = []
        queue.append(root)
        is_left_to_right = True  # 标记当前层的遍历方向
        
        while queue:
            size = len(queue)
            level_res = []
            # 将当前层的所有节点值按当前遍历方向存入level_res
            for _ in range(size):
                if is_left_to_right:
                    node = queue.pop(0)  # 从队首取节点
                    level_res.append(node.val)
                    # 为下一层准备：从左到右添加子节点
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()  # 从队尾取节点
                    level_res.append(node.val)
                    # 为下一层准备：从右到左添加子节点
                    if node.right:
                        queue.insert(0, node.right)
                    if node.left:
                        queue.insert(0, node.left)
            
            res.append(level_res)
            is_left_to_right = not is_left_to_right  # 切换下一层的遍历方向
            
        return res