# 3066. Minimum Operations to Exceed Threshold Value II

import heapq
from typing import List

class Solution:
    # 版本1
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        
        if heap[0] >= k:
            return 0

        count = 0
        while not heap[0] >= k:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            value = min(x, y) * 2 + max(x, y)
            heapq.heappush(heap, value)
            count += 1
        
        return count
    
    # 版本2：有点小问题[99,99,99] k = 100
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
    
        if not nums or nums[0] >= k:
            return 0

        count = 0
        while len(nums) >= 2:
            # 取出最小的两个数
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
        
            # 计算新值 (已知 x <= y，所以不需要使用min/max)
            value = x * 2 + y
            
            # 如果新值已经大于等于k，可以直接返回
            if value >= k:
                return count + 1
                
            heapq.heappush(nums, value)
            count += 1
        
        return -1