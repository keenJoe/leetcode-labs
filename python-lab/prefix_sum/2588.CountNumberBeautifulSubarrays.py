# 2588. Count the Number of Beautiful Subarrays

'''
    子数组：连续的元素序列
'''

from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # 使用前缀异或和 + 哈希表
        n = len(nums)
        count = 0
        prefix_xor = 0
        # 记录每个前缀异或和出现的次数
        xor_count = {0: 1}  # 初始值0出现1次
        
        for num in nums:
            # 计算当前的前缀异或和
            prefix_xor ^= num
            # 如果当前前缀异或和之前出现过，说明找到了美丽子数组
            count += xor_count.get(prefix_xor, 0)
            # 更新前缀异或和的出现次数
            xor_count[prefix_xor] = xor_count.get(prefix_xor, 0) + 1
            
        return count
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.beautifulSubarrays([4,2,1,3]))
