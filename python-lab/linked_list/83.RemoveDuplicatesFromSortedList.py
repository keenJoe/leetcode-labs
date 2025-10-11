# 83. Remove Duplicates from Sorted List

'''
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

方案一：使用单指针

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    # 使用递归
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 默认deleteDuplicates2返回的内容是不包括重复元素，head.next后没有重复元素
        head.next = self.deleteDuplicates2(head.next)

        # 如果head.val == head.next.val，则返回head.next，否则返回head
        return head.next if head.val == head.next.val else head

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
    result = solution.deleteDuplicates(head)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()