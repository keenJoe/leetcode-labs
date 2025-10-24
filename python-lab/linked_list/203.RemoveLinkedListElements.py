# 203. Remove Linked List Elements

'''
删除所有值为 val 的节点，返回链表的头节点

方案一：遍历
1、创建一个虚拟节点。因为头结点可能被删除。
2、然后从虚拟节点开始遍历，删除值为 val 的节点
3、返回虚拟节点的下一个节点

方案二：递归
1、如果头结点为空，则返回空
2、如果头结点的值为 val，则删除头结点，并返回下一个节点
3、如果头结点的值不为 val，则递归删除下一个节点
4、返回头结点
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        dummy_node = ListNode(0, head)

        current = dummy_node
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_node.next


    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        
        return head

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    val = 6
    result = solution.removeElements(head, val)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()