# 234. Palindrome Linked List

# Definition for singly-linked list.
from typing import Optional


"""
通过快慢指针找到链表中点，然后反转后半部分，然后比较前半部分和后半部分
如果不使用快慢指针，那么就需要计算链表的长度，然后再遍历找中间节点，然后再反转，然后再比较，时间复杂度为O(n)，空间复杂度为O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # 找到链表中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分
        prev = None
        # slow is the middle of the list
        current = slow
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        # 比较前半部分和后半部分
        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
