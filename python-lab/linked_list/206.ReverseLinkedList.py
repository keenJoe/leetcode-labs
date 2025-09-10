# 206. Reverse Linked List

from this import d
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
1、如果头结点为空，则直接返回 None
2、如果头结点不为空，则开始从头结点的下一个节点开始遍历
3、如果当前遍历的节点不为空，则将其插入到临时节点之后
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummyNode = ListNode(0, head)
        current = head.next

        # 关键的一步，如果没有就会造成环，内存溢出
        head.next = None
        while current:
            next = current.next
            current.next = dummyNode.next
            dummyNode.next = current
            current = next

        return dummyNode.next

    
    # 不需要断尾的解法
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        while head:
            # 保存下一个节点
            next = head.next
            # 将当前节点插入到 dummy 和 dummy.next 之间
            head.next = dummyNode.next
            dummyNode.next = head
            head = next
        return dummyNode.next


    # 双指针迭代
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            next = current.next
            current.next = prev
            prev, current = current, next
        return prev


    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        
        while head and head.next:
            # 先找到 dummy 要连接的节点
            dummy_to_connect = head.next
            # head 会作为最后一个节点
            head.next = head.next.next
            # dummy 要连接的节点，插入到 head 之后
            dummy_to_connect.next = dummyNode.next
            dummyNode.next = dummy_to_connect

        return dummyNode.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
    )
    reversed_head = solution.reverseList(head)
    print(reversed_head)
