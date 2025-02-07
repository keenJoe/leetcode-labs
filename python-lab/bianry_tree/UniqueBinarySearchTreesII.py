# 95. Unique Binary Search Trees II

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1. 递归，使用一个列表来存储所有可能的二叉搜索树。
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.generate(1, n)
    
    def generate(self, start, end):
        if start > end:
            return [None]
        allTrees = []
        for i in range(start, end + 1):
            leftTrees = self.generate(start, i - 1)
            rightTrees = self.generate(i + 1, end)
            for left in leftTrees:
                for right in rightTrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    allTrees.append(root)
        return allTrees
    
    # 2. 记忆化递归，使用一个字典来存储每个节点作为根节点时，二叉搜索树的数量。
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        # 使用字典来缓存结果
        memo = {}
        return self.generate_with_memo(1, n, memo)
    
    def generate_with_memo(self, start, end, memo):
        if start > end:
            return [None]
            
        # 检查是否已经计算过这个范围
        if (start, end) in memo:
            return memo[(start, end)]
            
        allTrees = []
        for i in range(start, end + 1):
            leftTrees = self.generate_with_memo(start, i - 1, memo)
            rightTrees = self.generate_with_memo(i + 1, end, memo)
            
            for left in leftTrees:
                for right in rightTrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    allTrees.append(root)
                    
        # 将结果存入缓存
        memo[(start, end)] = allTrees
        return allTrees
    

    # 3. 动态规划，使用一个字典来存储每个节点作为根节点时，二叉搜索树的数量。
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
            
        # dp[length][start] 存储从start开始，长度为length的所有可能的BST
        dp = {}
        
        # 初始化长度为1的情况
        for i in range(1, n + 1):
            dp[(1, i)] = [TreeNode(i)]
        
        # 长度从2到n
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                dp[(length, start)] = []
                end = start + length - 1
                
                # 枚举根节点
                for root_val in range(start, end + 1):
                    # 计算左子树长度和右子树长度
                    left_length = root_val - start
                    right_length = end - root_val
                    
                    # 获取左子树列表
                    left_trees = [None]
                    if left_length > 0:
                        left_trees = dp[(left_length, start)]
                    
                    # 获取右子树列表
                    right_trees = [None]
                    if right_length > 0:
                        right_trees = dp[(right_length, root_val + 1)]
                    
                    # 组合所有可能的左右子树
                    for left in left_trees:
                        for right in right_trees:
                            root = TreeNode(root_val)
                            root.left = self.clone_tree(left) if left else None
                            root.right = self.clone_tree(right) if right else None
                            dp[(length, start)].append(root)
        
        return dp[(n, 1)]
    
    def clone_tree(self, node):
        """深拷贝树节点"""
        if not node:
            return None
        new_node = TreeNode(node.val)
        new_node.left = self.clone_tree(node.left)
        new_node.right = self.clone_tree(node.right)
        return new_node