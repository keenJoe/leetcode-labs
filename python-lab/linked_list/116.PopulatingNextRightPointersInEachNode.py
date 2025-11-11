# 116. Populating Next Right Pointers in Each Node


'''
1、使用层序遍历
2、在每一层，将每个节点的 next 指针指向同一层右侧的节点

其他无论是递归还是迭代，都不太适合这道题。
因为不能跨不同子树找下一个节点。
'''


# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == size - 1:
                    node.next = None
                else:
                    node.next = queue[0]
        return root


    # 也是层序遍历
    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        # 从根节点开始，逐层处理
        leftmost = root
        
        while leftmost.left:  # 当还有下一层时
            # 遍历当前层，为下一层建立连接
            head = leftmost
            while head:
                # 连接1：左子节点 -> 右子节点
                head.left.next = head.right
                
                # 连接2：右子节点 -> next节点的左子节点（跨父节点连接）
                if head.next:
                    head.right.next = head.next.left
                
                # 移动到当前层的下一个节点
                head = head.next
            
            # 移动到下一层的最左节点
            leftmost = leftmost.left
        
        return root

if __name__ == "__main__":
    solution = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    solution.connect(root)
    print(root)
        