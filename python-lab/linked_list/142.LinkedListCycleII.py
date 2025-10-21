# 142. Linked List Cycle II

'''
返回链表开始入环的第一个节点

方案一：使用哈希表
1、遍历链表，将节点存储到哈希表中；
2、如果节点在哈希表中，则返回节点；
3、如果节点不在哈希表中，则将节点存储到哈希表中；
4、如果遍历完链表，则返回None；

方案二：使用快慢指针
1、使用快慢指针，快指针每次走两步，慢指针每次走一步；
2、如果快慢指针相遇，则说明有环；
3、如果快指针走到None，则说明没有环；
4、如果快慢指针相遇，则返回相遇节点；
5、如果快指针走到None，则返回None；

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycleUsingSet(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head
        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next
        return None

    def detectCycleUsingTwoPointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 边界情况处理
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head  # ✅ 两个指针都从 head 开始
        
        # 第一阶段：判断是否有环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # 相遇说明有环
                break
        
        # 如果没有环，返回 None
        if fast is None or fast.next is None:
            return None
        
        # 第二阶段：找环的入口
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head.next.next
    print(solution.detectCycleUsingSet(head).val)
    print(solution.detectCycleUsingTwoPointers(head).val)