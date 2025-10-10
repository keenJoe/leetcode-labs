# 61. Rotate List

'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
其实就是将链表末尾的 k 个节点移动到链表头部。
但是要注意，如果 k 大于链表长度，则需要取模。
但是取模需要计算链表长度，然后取模。
但是计算链表长度需要遍历链表，所以时间复杂度为 O(n)。

如何不计算链表的长度，而是直接找到需要移动的节点位置？
1、使用快慢指针
2、快指针先走 k 步，然后慢指针再开始走
3、当快指针到达末尾时，慢指针恰好到达需要移动的节点位置
4、移动节点

但是如果 K 步已经超过链表的长度，那么需要继续走，直到快指针到达末尾。
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 计算链表长度
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        k = k % length
        if k == 0:
            return head

        slow = head
        fast = head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head
        
        return new_head

    def rotateRightUsingRing(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 计算链表长度
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # 构成环
        tail.next = head

        k = k % length
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    result = solution.rotateRight(head, k)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()
