# 3287. Find the Maximum Sequence Value of Array

from typing import List

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2 * k:
            return 0
            
        def findORs(arr: List[int], k: int) -> List[int]:
            # 使用数字而不是集合来存储OR值，因为OR操作的结果是唯一的
            dp = []
            prev = [set() for _ in range(k + 1)]
            prev[0].add(0)
            
            # 计算所有可能的k个数的OR值
            for i, num in enumerate(arr):
                # 从大到小遍历j避免重复计算
                for j in range(min(k - 1, i + 1), -1, -1):
                    # 对于当前数字num，将其与之前的所有可能OR值进行OR操作
                    for x in prev[j]:
                        prev[j + 1].add(x | num)
                # 存储当前位置能够得到的所有k个数的OR值
                dp.append(prev[k].copy())
            
            return dp
        
        # 计算从左到右和从右到左的所有可能OR值
        forward = findORs(nums, k)
        backward = findORs(nums[::-1], k)
        
        ans = 0
        # 枚举分割点，计算最大XOR值
        for i in range(k - 1, n - k):
            # 使用生成器表达式替代列表推导，节省内存
            ans = max(ans, max(a ^ b for a in forward[i] for b in backward[n - i - 2]))
        
        return ans