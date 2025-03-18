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
    
    # 方法1：使用双栈实现
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack1 = [root]
        stack2 = []  # 用于存储访问顺序的栈
        
        # 先序遍历变形：根->右->左，存入stack2
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            # 左子树先入栈，这样出栈时右子树先处理
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        # 从stack2取出节点，顺序正好是：左->右->根
        while stack2:
            result.append(stack2.pop().val)
            
        return result
    
    # 方法2：单栈实现，使用上次访问节点标记
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = []
        current = root
        last_visited = None  # 记录上次访问的节点
        
        while current or stack:
            # 遍历到最左节点
            if current:
                stack.append(current)
                current = current.left
            else:
                # 查看栈顶节点
                peek_node = stack[-1]
                
                # 如果右子树存在且未访问过，访问右子树
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    # 访问当前节点
                    result.append(peek_node.val)
                    last_visited = stack.pop()
        
        return result
    
    # 方法3：使用标记法
    def postorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [(root, False)]  # (节点, 是否已访问过右子树)
        
        while stack:
            node, visited = stack.pop()
            
            # 如果是叶子节点或右子树已访问过
            if not node.left and not node.right or visited:
                result.append(node.val)
            else:
                # 再次入栈，标记为已访问
                stack.append((node, True))
                
                # 右子树先入栈，左子树后入栈(这样左子树会先出栈)
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        
        return result