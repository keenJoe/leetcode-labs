# 109. Convert Sorted List to Binary Search Tree

'''
给定一个单链表的头节点head ，其中的元素按升序排序 ，将其转换为平衡二叉搜索树。

输入: head = [-10,-3,0,5,9]
输出: [0,-3,9,-10,null,5]
解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。

因为链表已经是有序的升序的链表，所以可以考虑使用二分法来构建平衡二叉搜索树。
1、找到链表的中点，作为根节点，开始构建平衡二叉树
    使用快慢指针的方式找中点
2、递归构建左子树和右子树
3、然后返回 head
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
#         if not head:
#             return None

#         # 找到链表的中点
#         slow = fast = head
#         prev = None
#         while fast.next and fast.next.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next
        
#         root = TreeNode(prev.val)
#         prev.next = None
#         current = head
#         while current != prev:
#             current = current.next
#         current.next = None
#         root.left = self.sortedListToBST(head)
#         root.right = self.sortedListToBST(slow)
#         return root
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:  # 只有一个节点
            return TreeNode(head.val)
        
        # 使用快慢指针找到中点
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next  # 快指针每次移动两步，这个非常关键。之前自己的移动一步根本做不到找中点
        
        # slow 是中点，用它作为根节点
        root = TreeNode(slow.val)
        
        # 断开左半部分
        if prev:
            prev.next = None
        
        # 递归构建左右子树
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)  # 右子树从 slow.next 开始
        
        return root

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)
    print(solution.sortedListToBST(head))