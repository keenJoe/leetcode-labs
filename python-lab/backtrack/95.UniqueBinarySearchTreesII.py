# 95. Unique Binary Search Trees II

'''
    给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
    输入: 3
    输出:
    [
        [1,null,3,2,null,4,null,null,5,null,null],
        [3,2,4,1,null,5,null,null,null,null,null],
        [3,2,4,1,null,5,null,null,null,null,null],
        [2,1,3,null,4,null,5,null,null,null,null]
    ]
    解释:
    以上的输出对应以下 5 种不同结构的二叉搜索树：

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
    以每一个数字为根节点，生成所有可能的二叉搜索树
    先排序，1,2,3
    以1为例，左子树为空，右子树为2,3。以1为根节点的树 = 左子树（1）* 右子树（2,3）
    以2为例，左子树为1，右子树为3。以2为根节点的树 = 左子树（1）* 右子树（3）
    以3为例，左子树为1,2，右子树为空。以3为根节点的树 = 左子树（1,2）* 右子树（3）
    所以，以1,2,3为根节点的树 = 左子树（1）* 右子树（2,3） + 左子树（1,2）* 右子树（3） + 左子树（1）* 右子树（2,3）
'''



# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    #     res = []
    #     path = []

    #     def backtrack(start, end):
    #         if len(path) == n and start > end:
    #             res.append(path[:])
    #             return
            
    #         for i in range(1, n + 1):
    #             path.append(i)
    #             backtrack(start, i - 1)
    #             backtrack(i + 1, end)
    #             path.pop()
        
    #     backtrack(1, n)
    #     return res

    # 可以添加记忆化来避免重复计算
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        
        memo = {}
        def backtrack(start: int, end: int) -> List[TreeNode]:
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = backtrack(start, i - 1)
                right_trees = backtrack(i + 1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            
            memo[(start, end)] = all_trees
            return all_trees
        return backtrack(1, n)
    
if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees(3))