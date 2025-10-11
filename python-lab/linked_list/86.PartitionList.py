# 86. Partition List

'''
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

方案一
使用两个链表
链表一存放小于 x 的节点，链表二存放大于等于 x 的节点
最后将链表一和链表二连接起来
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        # 构建
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        # 连接
        before.next = after_head.next
        # 断尾，防止环
        after.next = None

        return before_head.next

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    x = 3
    result = solution.partition(head, x)
    while result:
        print(result.val, end=" ")
        result = result.next