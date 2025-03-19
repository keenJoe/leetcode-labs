# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
from collections import deque
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
            # 添加到尾部
            res[level].append(root.val)
        else:
            # 从右到左，添加到头部
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
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        is_reverse = False
        
        while queue:
            level = []
            # 当前层的所有节点
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                # 子节点永远从左到右入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 如果需要反转，直接反转level
            if is_reverse:
                level.reverse()
            
            result.append(level)
            is_reverse = not is_reverse
            
        return result
    
    # 方法2：使用双端队列处理每一层
    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        level_number = 0
        
        while queue:
            level = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                
                # 根据层号决定添加到level的哪一端
                if level_number % 2 == 0:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                    
                # 子节点永远从左到右入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level))
            level_number += 1
            
        return result
    
    # 方法3：使用列表推导式和切片
    def zigzagLevelOrder3(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        level = [root]
        level_number = 0
        
        while level:
            # 获取当前层的值
            result.append([node.val for node in level][::(-1 if level_number % 2 else 1)])
            
            # 生成下一层节点
            level = [child for node in level 
                    for child in (node.left, node.right) if child]
            
            level_number += 1
            
        return result