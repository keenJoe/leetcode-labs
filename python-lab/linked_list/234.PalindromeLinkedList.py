# 234. Palindrome Linked List

'''
方案一：
    1、使用快慢指针找到链表中点
    2、反转后半部分
    3、比较前半部分和后半部分
    4、返回是否是回文
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分
        prev = None
        current = slow
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    # 使用额外空间，利用了 Python 的切片特性
    def isPalindromeUsingExtraSpace(self, head: Optional[ListNode]) -> bool:
        """
        时间复杂度：O(n)
        空间复杂度：O(n)
        优点：代码简洁，易于理解
        缺点：使用额外空间
        """
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        return values == values[::-1]  # 或用双指针

    # 这个实现太妙了
    # 先走到链表的末尾，然后从末尾开始比较
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        时间复杂度：O(n)
        空间复杂度：O(n) - 递归调用栈
        优点：代码优雅
        缺点：递归深度受限，可能栈溢出
        """

        # 这个闭包的妙用，可以在递归的所有函数中共享变量
        self.front_pointer = head
        
        def recursively_check(current_node):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        
        return recursively_check(head)

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(solution.isPalindrome(head))