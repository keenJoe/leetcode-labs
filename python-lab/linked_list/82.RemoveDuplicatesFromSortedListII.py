# 82. Remove Duplicates from Sorted List II

'''
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
如果一个元素出现重复，那么完全删掉，不再保留任何痕迹。

方案一：使用双指针
1、慢指针从 dummy 开始，快指针从 head 开始；
2、慢指针的作用是记录不重复的元素，当删除重复元素时，可以记录当前元素的前一个元素；
3、快指针的作用是遍历链表，找到重复的元素；
4、如果快指针遇到重复的元素，则慢指针不动，快指针继续遍历，直到找到不重复的元素；
5、如果快指针遇到不重复的元素，则慢指针移动到快指针的位置，快指针继续遍历；
6、重复上述步骤，直到快指针遍历到链表的末尾；
7、返回 dummy.next；

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while fast:
            # 找到重复的元素
            while fast.next and fast.val == fast.next.val:
                fast = fast.next

            # 跳出循环，当前的 fast.next 和之前的fast 不同了
            if slow.next != fast:
                # 如果slow.next != fast，代表有重复元素，移动慢指针，删除了重复元素
                slow.next = fast.next
            else:
                # 如果slow.next == fast，代表没有重复元素，移动慢指针，没有需要删除的元素
                slow = slow.next
            fast = fast.next

        return dummy.next
            

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    result = solution.deleteDuplicates(head)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()