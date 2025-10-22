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
        if not head or not head.next:
            return
        
        # 步骤1：使用快慢指针找到链表中点
        # slow最终会停在前半部分的最后一个节点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 步骤2：反转后半部分链表
        # 将链表从中间断开
        second = slow.next
        slow.next = None
        
        # 反转后半部分
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev  # second 现在指向反转后链表的头节点
        
        # 步骤3：合并两个链表
        first = head
        while second:  # 只需要判断 second，因为后半部分长度 <= 前半部分
            # 保存下一个节点
            first_next = first.next
            second_next = second.next
            
            # 交替连接
            first.next = second
            second.next = first_next
            
            # 移动指针
            first = first_next
            second = second_next


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