# 382. Linked List Random Node

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def __init__(self, head: Optional[ListNode]):
        pass

    # 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。
    def getRandom(self) -> int:
        pass

if __name__ == '__main__':
    solution = Solution()
    solution.getRandom()
    print(solution.getRandom())
    print(solution.getRandom())