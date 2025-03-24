# 437. Path Sum III

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional, Dict
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 使用字典记录前缀和及其出现次数
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # 初始化前缀和为0的情况
        
        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0
            
            # 计算当前路径和
            curr_sum += node.val
            # 寻找是否存在前缀和，使得 curr_sum - prefix_sum = targetSum
            count = prefix_sum[curr_sum - targetSum]
            
            # 将当前前缀和加入字典
            prefix_sum[curr_sum] += 1
            
            # 递归处理左右子树
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # 回溯：移除当前前缀和
            prefix_sum[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)

    def create_tree(self, values: list) -> Optional[TreeNode]:
        """辅助函数：从列表创建二叉树"""
        if not values:
            return None
            
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            # 创建左子节点
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            # 创建右子节点
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

if __name__ == "__main__":
    s = Solution()
    values = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root = s.create_tree(values)
    targetSum = 8
    print(s.pathSum(root, targetSum))  # 应输出 3