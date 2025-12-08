# 1004. Max Consecutive Ones III

'''
给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数 。

示例 1：
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。


记录已经翻了多少个 0 ，如果超过 k ，则需要移动 left 指针，直到当前的元素的频率满足 k 值
但是移动到哪里呢？所以还需要一个 map 记录每个 0 的位置，移动到最左边的 0 的下一个位置，然后继续移动 right 指针
不应该使用 map，而应该使用队列，因为队列可以保证每次移动到最左边的 0 的下一个位置
'''


from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0
        count = 0
        zero_positions = []

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_positions.append(right)
                count += 1

            while count > k:
                if nums[left] == 0:
                    zero_positions.pop(0)
                    count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    
    # 不需要队列，因为不会改变0的数值
    def longestOnes1(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0
        zero_count = 0  # 记录当前窗口中0的个数
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # 如果0的个数超过k，移动左指针
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

    def longestOnes2(self, nums: List[int], k: int) -> int:
        left = 0
        
        for right in range(len(nums)):
            # 遇到0时，k减1（表示用掉一次翻转机会）
            if nums[right] == 0:
                k -= 1
            
            # 如果k小于0，说明翻转机会用完了
            if k < 0:
                # 移动左指针
                if nums[left] == 0:
                    k += 1  # 恢复一次翻转机会
                left += 1
        
        # 最终right遍历到末尾，left是窗口起始位置
        return right - left + 1

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(solution.longestOnes(nums, k))