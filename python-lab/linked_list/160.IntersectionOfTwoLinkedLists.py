# 160. Intersection of Two Linked Lists

'''
<<<<<<< HEAD
方案一：
    1、分别计算两个链表的长度；
    2、计算两个链表长度的差值
    3、让长链表的指针先走差值步
    4、然后两个指针一起走，直到相遇
    5、返回相遇节点
方案二：
    1、两个指针分别从头遍历两个链表
    2、如果两个指针相遇，则返回相遇节点
    3、如果两个指针没有相遇，则继续遍历另一个链表，直到相遇
    4、返回相遇节点
'''

from typing import Optional

# Definition for singly-linked list.
=======
1、分别计算两个链表的长度
2、计算两个链表的差值
3、然后让长度较长的链表先走差值步
4、然后两个链表同时走，如果两个链表的节点相同，则返回节点
5、如果两个链表没有相同节点，则返回None
'''

# Definition for singly-linked list.
from typing import Optional


>>>>>>> e2ded62 (update)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
<<<<<<< HEAD
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

if __name__ == '__main__':
    solution = Solution()
    headA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
    headB = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))
    print(solution.getIntersectionNode2(headA, headB).val)
=======
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        diff = abs(lenA - lenB)
        if lenA > lenB:
            headA = self.moveHead(headA, diff)
        else:
            pass


        return None
    
    def getLength(self, head: ListNode) -> int:
        if head is None:
            return 0
        
        length = 0
        while head:
            length += 1
            head = head.next
        return length


if __name__ == "__main__":
    solution = Solution()
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(6)
    headB.next = ListNode(7)
    headB.next.next = ListNode(8)
    headB.next.next.next = ListNode(9)
    headB.next.next.next.next = ListNode(10)
    print(solution.getIntersectionNode(headA, headB))
>>>>>>> e2ded62 (update)
