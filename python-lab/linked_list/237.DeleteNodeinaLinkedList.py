# 237. Delete Node in a Linked List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        # 后一个值覆盖前一个值
        node.val = node.next.val
        # 然后删除后一个节点
        node.next = node.next.next

if __name__ == '__main__':
    solution = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    solution.deleteNode(node.next.next)
    while node:
        print(node.val, end=' ')
        node = node.next