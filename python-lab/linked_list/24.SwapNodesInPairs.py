# 24. Swap Nodes in Pairs

'''
1、需要一个 dummy_node 节点
2、需要一个 current 节点，用于遍历链表
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        current = dummy_node
        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first

            current.next = second
            current = first

        return dummy_node.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    result = solution.swapPairs(head)
    while result:
        print(result.val, end=" ")
        result = result.next