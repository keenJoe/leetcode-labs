# 143. Reorder List

'''
1、先找到链表的中点
    使用快慢指针找链表的中点
2、反转链表的后半部分，反转后半部分
3、合并链表
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 现在的 slow 就是中间点
        second_head = slow.next
        # 反转后半部分
        after = None
        current = second_head
        while current:
            next = current.next
            current.next = after
            after = current
            current = next
        second_head = after

        slow.next = None
        first_head = head

        while first_head and second_head:
            first_next = first_head.next
            second_next = second_head.next
            first_head.next = second_head
            second_head.next = first_next
            first_head = first_next
            second_head = second_next
        
        return head


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution.reorderList(head)
    while head:
        print(head.val, end=" ")
        head = head.next