# 23. Merge k Sorted Lists


'''
分治法合并多个链表
1、两两进行合并
2、然后将合并后的链表加入到 list 中
3、合并完原 list 后，将新 list 指向原 list
4、继续遍历原 list 进行合并


归并法合并链表
1、将链表分成两部分
2、递归合并两部分
3、合并两部分


使用堆合并链表
'''

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 分治法
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(self.mergetTwoList(list1, list2))

            lists = merged_list

        return lists[0]
    
    # 归并法
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeKListsHelper(lists, 0, len(lists) - 1)

    def mergeKListsHelper(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        if left > right:
            return None
        
        mid = (left + right) // 2
        left_list = self.mergeKListsHelper(lists, left, mid)
        right_list = self.mergeKListsHelper(lists, mid + 1, right)

        return self.mergetTwoList(left_list, right_list)


    def mergetTwoList(self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        current = dummy_node
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
            elif list1:
                current.next = list1
                list1 = list1.next
            elif list2:
                current.next = list2
                list2 = list2.next
            current = current.next

        return dummy_node.next
    
    def mergeKListsHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        方法4：堆/优先队列法
        
        使用最小堆维护每个链表的当前最小节点
        时间复杂度：O(N*log(k))
        空间复杂度：O(k)
        """
        if not lists:
            return None
        
        # 创建最小堆，存储 (节点值, 节点索引, 节点)
        heap = []
        
        # 将每个链表的第一个节点加入堆
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            # 取出最小值节点
            val, list_idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # 如果该链表还有下一个节点，将其加入堆
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    result = solution.mergeKLists(lists)
    while result:
        print(result.val, end=" ")
        result = result.next