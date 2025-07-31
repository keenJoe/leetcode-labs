# 19. Remove Nth Node From End of List

'''
删除倒数第n个节点，返回头节点·
方案一
1、计算链表长度
2、计算需要删除的节点位置
3、删除节点

方案二
1、使用快慢指针
2、快指针先走 N 步，然后慢指针再开始走
3、当快指针到达末尾时，慢指针恰好到达被删除节点的前一个节点
4、删除节点

⚠️：被删除的节点可能是头节点，所以需要一个哑节点来处理这种情况
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)

        slow = dummy_head
        fast = dummy_head
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy_head.next

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    result = solution.removeNthFromEnd(head, n)
    while result:
        print(result.val, end=" ")
        result = result.next