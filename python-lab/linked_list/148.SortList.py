<<<<<<< HEAD
# 148. Sort List
=======
# 148. Sort List

''''''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    print(solution.sortList(head))
>>>>>>> e2ded62 (update)
