# 160. Intersection of Two Linked Lists


"""
heada = a1 -> a2 -> c1 -> c2 -> c3 => b1 -> b2 -> b3 -> c1 -> c2 -> c3
headb = b1 -> b2 -> b3 -> c1 -> c2 -> c3 => a1 -> a2 -> c1 -> c2 -> c3
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        pA = headA
        pB = headB
        
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA