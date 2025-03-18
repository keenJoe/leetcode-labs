# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 中序遍历：左子树 -> 根节点 -> 右子树
class Solution:
    # 递归
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs_inorder(root, res)
        return res

    def dfs_inorder(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if root:
            self.dfs_inorder(root.left, res)
            res.append(root.val)
            self.dfs_inorder(root.right, res)
        return res

    # 迭代，这个方法自己没有用过
    # 这个方法和Morris遍历类似，但是Morris遍历是O(1)空间复杂度，这个方法是O(n)空间复杂度
    def inorderTraversal_using_stack(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                if not node.left:
                    res.append(node.val)
                    stack.append(node.right)
                else:
                    stack.append(node)
                    stack.append(node.left)
                    # 防止重复访问，这个节点已经访问过
                    node.left = None

        return res
    

    def inorderTraversal_using_stack_2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res
    
    # 方法2：节点标记法
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        stack = [(root, False)]  # (节点, 是否已访问)
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                # 如果节点已被访问过，直接添加到结果
                result.append(node.val)
            else:
                # 中序：右->根->左，压栈后变成左->根->右
                if node.right:
                    stack.append((node.right, False))
                    
                # 标记根节点为已访问，再次入栈
                stack.append((node, True))
                
                if node.left:
                    stack.append((node.left, False))
                    
        return result
    
    # Morris遍历，O(1)空间复杂度
    # 这个方法和迭代方法类似，但是Morris不再使用栈，那么当根节点的左右节点都为空，需要回到根节点，然后开始遍历右节点。但是因为当前节点的左节点不为空，会继续遍历左节点。这样就会形成一个环。
    # 和前序遍历的Morris对比，前序遍历的Morris是先遍历根节点，然后遍历右节点。而中序遍历的Morris是先遍历左节点，然后遍历根节点。
    def inorderTraversal_using_morris(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
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
                    res.append(cur.val)
                    cur = cur.right

        return res

    # 方法4：使用颜色标记法（统一处理前序、中序、后序）
    def inorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        WHITE, GRAY = 0, 1  # WHITE表示首次访问，GRAY表示再次访问
        result = []
        stack = [(WHITE, root)]
        
        while stack:
            color, node = stack.pop()
            
            if not node:
                continue
                
            if color == WHITE:
                # 中序：右->根->左，压栈后变成左->根->右
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))  # 将节点设为GRAY，再次访问时处理
                stack.append((WHITE, node.left))
            else:
                # GRAY节点直接访问
                result.append(node.val)
                
        return result