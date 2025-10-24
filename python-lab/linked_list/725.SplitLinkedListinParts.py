# 725. Split Linked List in Parts

'''
输入：head = [1,2,3,4,5,6,7,8,9,10], k = 3
输出：[[1,2,3,4],[5,6,7],[8,9,10]]

输入：head = [1,2,3], k = 5
输出：[[1],[2],[3],[],[]]


k 表示要分割的链表的个数，也代表最终的链表数量
所以遍历原链表，然后构建 K 个链表
'''

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 步骤1：计算链表的总长度
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # 步骤2：计算每部分的基本长度和需要额外分配节点的部分数
        base_size = length // k  # 每部分的基本长度
        extra = length % k       # 前 extra 个部分需要多一个节点
        
        # 步骤3：初始化结果列表
        result = []
        current = head
        
        # 步骤4：遍历 k 个部分进行切分
        for i in range(k):
            # 记录当前部分的头节点
            part_head = current
            result.append(part_head)
            
            # 计算当前部分的长度
            # 前 extra 个部分的长度是 base_size + 1，后面的是 base_size
            part_size = base_size + (1 if i < extra else 0)
            
            # 移动到当前部分的最后一个节点
            for j in range(part_size - 1):
                if current:
                    current = current.next
            
            # # 断开当前部分和下一部分的连接
            # if current:
            #     next_part_head = current.next
            #     current.next = None  # 断开连接
            #     current = next_part_head
            if current:
                current, current.next = current.next, None
            else:
                current = None
        
        return result


if __name__ == '__main__':
    solution = Solution()
    
    # 测试用例1：[1,2,3,4,5,6,7,8,9,10], k = 3
    # 长度10，分成3部分：10 // 3 = 3，10 % 3 = 1
    # 第一部分4个节点，后两部分各3个节点
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, 
            ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    k1 = 3
    result1 = solution.splitListToParts(head1, k1)
    print("测试用例1:")
    for part in result1:
        temp = part
        print("[", end="")
        while temp:
            print(temp.val, end="")
            if temp.next:
                print(",", end="")
            temp = temp.next
        print("]", end=" ")
    print()
    
    # 测试用例2：[1,2,3], k = 5
    # 长度3，分成5部分：3 // 5 = 0，3 % 5 = 3
    # 前3部分各1个节点，后2部分为空
    head2 = ListNode(1, ListNode(2, ListNode(3)))
    k2 = 5
    result2 = solution.splitListToParts(head2, k2)
    print("\n测试用例2:")
    for part in result2:
        temp = part
        print("[", end="")
        while temp:
            print(temp.val, end="")
            if temp.next:
                print(",", end="")
            temp = temp.next
        print("]", end=" ")
    print()