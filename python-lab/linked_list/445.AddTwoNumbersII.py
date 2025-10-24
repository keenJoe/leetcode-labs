# 445. Add Two Numbers II

'''
将两个链表反转，再从头遍历相加，最后再反转链表
'''

# Definition for singly-linked list.
from calendar import c
from operator import ne
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 反转两个链表
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        # 两个链表相加
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10
            
            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return self.reverseList(dummy.next)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev

if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(5, ListNode(3, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=' ')
        result = result.next