# 110. Balanced Binary Tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1. 递归，自顶向下，需要计算每一个节点的高度，然后判断是否平衡
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    

    # 2. 递归，自底向上，不需要计算每一个节点的高度，只需要判断是否平衡
    def isBalanced_2(self, root: Optional[TreeNode]) -> bool:
        return self.height_2(root) >= 0
    
    def height_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.height_2(root.left)
        right_height = self.height_2(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    

    # 3. 迭代
    def isBalanced_iter(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # 使用字典存储每个节点的高度
        height_map = {}
        stack = []
        last_visited = None
        current = root
        
        while stack or current:
            # 遍历到最左节点
            while current:
                stack.append(current)
                current = current.left
            
            # 查看栈顶节点
            peek = stack[-1]
            
            # 如果右子树存在且未访问过，则访问右子树
            if peek.right and peek.right != last_visited:
                current = peek.right
            else:
                # 处理当前节点
                node = stack.pop()
                
                # 计算左右子树高度
                left_height = height_map.get(node.left, 0)
                right_height = height_map.get(node.right, 0)
                
                # 检查是否平衡
                if abs(left_height - right_height) > 1:
                    return False
                    
                # 更新当前节点的高度
                height_map[node] = max(left_height, right_height) + 1
                
                last_visited = node
                current = None
        
        return True
    
    # 方法2：使用层序遍历（自底向上）
    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        from collections import deque
        
        # 使用队列存储节点和它们的层级
        queue = deque([(root, 1)])
        height_map = {}  # 存储节点高度
        
        while queue:
            node, level = queue.popleft()
            
            # 如果有子节点，加入队列
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            
            # 如果没有子节点，开始回溯计算高度
            if not node.left and not node.right:
                height_map[node] = 1
            elif node.left in height_map and node.right in height_map:
                # 两个子节点都已处理完
                left_height = height_map.get(node.left, 0)
                right_height = height_map.get(node.right, 0)
                
                if abs(left_height - right_height) > 1:
                    return False
                    
                height_map[node] = max(left_height, right_height) + 1
                queue.append((node, level))  # 重新加入队列等待处理父节点
        
        return True
    
    # 方法3：使用栈（更简洁的实现）
    def isBalanced3(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, False)]
        heights = {None: 0}  # 使用None作为空节点的高度
        
        while stack:
            node, visited = stack.pop()
            
            if not node:
                continue
                
            if visited:
                # 计算左右子树高度
                left_height = heights[node.left]
                right_height = heights[node.right]
                
                if abs(left_height - right_height) > 1:
                    return False
                    
                heights[node] = max(left_height, right_height) + 1
            else:
                # 后序遍历顺序：左->右->根
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        
        return True

# 测试代码
if __name__ == "__main__":
    # 创建测试用例
    def create_test_tree1():
        #     3
        #    / \
        #   9  20
        #     /  \
        #    15   7
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        return root
    
    def create_test_tree2():
        #        1
        #       / \
        #      2   2
        #     /     \
        #    3       3
        #   /         \
        #  4           4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.right.right.right = TreeNode(4)
        return root
    
    s = Solution()
    
    # 测试平衡树
    balanced_tree = create_test_tree1()
    print("平衡树测试:")
    print("方法1:", s.isBalanced(balanced_tree))   # 应该返回 True
    print("方法2:", s.isBalanced2(balanced_tree))  # 应该返回 True
    print("方法3:", s.isBalanced3(balanced_tree))  # 应该返回 True
    
    # 测试不平衡树
    unbalanced_tree = create_test_tree2()
    print("\n不平衡树测试:")
    print("方法1:", s.isBalanced(unbalanced_tree))   # 应该返回 False
    print("方法2:", s.isBalanced2(unbalanced_tree))  # 应该返回 False
    print("方法3:", s.isBalanced3(unbalanced_tree))  # 应该返回 False
    
    # 测试空树
    print("\n空树测试:")
    print("方法1:", s.isBalanced(None))   # 应该返回 True
    print("方法2:", s.isBalanced2(None))  # 应该返回 True
    print("方法3:", s.isBalanced3(None))  # 应该返回 True
