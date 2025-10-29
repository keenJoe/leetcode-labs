# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        # 计算链表的长度
        length_a = self.getLength(headA)
        length_b = self.getLength(headB)

        # 计算链表的差值
        diff = length_a - length_b
        if diff > 0:
            for _ in range(diff):
                headA = headA.next
        else:
            for _ in range(-diff):
                headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA

    def getLength(self, head: ListNode) -> int:
        length = 0

        current = head
        while current:
            length += 1
            current = current.next
        
        return length

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        p_a = headA
        p_b = headB
        
        while p_a != p_b:
            p_a = p_a.next if p_a else headB
            p_b = p_b.next if p_b else headA
        
        return p_a