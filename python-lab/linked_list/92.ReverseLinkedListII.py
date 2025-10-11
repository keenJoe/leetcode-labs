# 92. Reverse Linked List II
# 反转链表 II

'''
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

反转整个链表的一个片段，而不是整个链表


先找到 left 和 right 的位置，记录 left 前一个节点和 right 后一个节点，因为反转后的链表和原来的链表连接需要用到
然后剩下的就是反转链表
最后将反转后的链表和原来的链表连接起来

'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     index = 0
    #     left_prev = None
    #     right_next = None
    #     current = head
    #     while current:
    #         if index == left - 1:
    #             left_prev = current
    #         if index == right:
    #             right_next = current.next
    #         current = current.next
    #         index += 1

    #     current = left_prev.next
    #     prev = right_next
    #     while current != right_next:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next

    #     left_prev.next = prev
    #     current.next = right_next
    #     return head
    
    # 不需要提前确认右边界
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 使用虚拟头节点简化边界处理
        dummy = ListNode(0)
        dummy.next = head
        
        # 找到left前一个节点
        left_prev = dummy
        for _ in range(left - 1):
            left_prev = left_prev.next
        
        # 开始反转
        current = left_prev.next
        prev = None
        for _ in range(right - left + 1):
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        # 连接反转后的链表
        left_prev.next.next = current  # 原left节点连接到right后
        left_prev.next = prev          # left前节点连接到新头
        
        return dummy.next
        

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left = 2
    right = 4
    result = solution.reverseBetween(head, left, right)
    while result:
        print(result.val, end=" ")
        result = result.next