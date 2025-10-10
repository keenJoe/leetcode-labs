# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    result = solution.deleteDuplicates(head)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()