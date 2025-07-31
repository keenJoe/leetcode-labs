# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
            elif list1:
                current.next = list1    
                list1 = list1.next
            elif list2:
                current.next = list2
                list2 = list2.next
            current = current.next

        return dummy_head.next


if __name__ == "__main__":
    solution = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    result = solution.mergeTwoLists(list1, list2)
    while result:
        print(result.val, end=" ")
        result = result.next
        