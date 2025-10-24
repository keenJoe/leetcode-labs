# 147. Insertion Sort List

'''
插入排序：默认第一个节点是一个有序的链表，从第二个节点开始，遍历前面有序链表，然后找到位置，将节点插入到有序链表中。
一定需要一个循环遍历整个链表，可以从第二个链表开始遍历。如果第二个链表为 none，则直接返回 head，排序结束
然后开始进行插入排序。
插入排序也需要一个循环，从第一个节点开始，找到合适的位置，将节点插入到有序链表中。
是不是可以先和前面的节点进行比较，如果比前一个节点大，则不需要插入，直接跳过。

'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        prev = head
        current = head.next
        while current:
            if current.val < prev.val:
                # # 剩余未排序链表的头结点
                # next = current.next
                # 临时节点，用于遍历
                temp = dummy_node
                while temp.next and temp.next.val < current.val:
                    temp = temp.next
                # 连接 prev 和 next
                prev.next = current.next
                # 将 current 插入到 temp 之后
                current.next = temp.next
                # 连接 temp 和 current
                temp.next = current
                # 移动到下一个节点继续
                current = prev.next
            else:
                prev = current
                current = current.next

        return dummy_node.next

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    solution.insertionSortList(head)
    while head:
        print(head.val, end=" ")
        head = head.next