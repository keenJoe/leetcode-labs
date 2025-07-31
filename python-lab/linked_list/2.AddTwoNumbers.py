# 2. Add Two Numbers

'''
同时遍历两个链表，然后要注意进位问题
同时需要一个 dummy_head 来记录结果链表的头节点
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head

        carry = 0
        # 只要有一个链表没有结束，或者有进位，就继续遍历
        while l1 or l2 or carry:
            # 获取当前位的值，如果链表已经结束，则使用0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # 计算当前位的和，并更新进位
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10
            # 创建新节点并添加到结果链表
            current.next = ListNode(digit)
            current = current.next
            # 移动到下一个节点（如果存在）
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next
