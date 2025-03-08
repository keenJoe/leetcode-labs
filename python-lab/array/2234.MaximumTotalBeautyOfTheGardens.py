# 2234. Maximum Total Beauty of the Gardens

from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        # 将所有超过target的花园数量限制为target
        flowers = [min(f, target) for f in flowers]
        # 按花的数量排序
        flowers.sort()
        n = len(flowers)
        
        # 如果所有花园都已完善，直接返回结果
        if flowers[0] >= target:
            return full * n
            
        # 如果没有花园，返回0
        if n == 0:
            return 0
            
        # 单花园特殊处理
        if n == 1:
            if flowers[0] + newFlowers >= target:
                return max(full, partial * min(target - 1, flowers[0] + newFlowers))
            else:
                return partial * (flowers[0] + newFlowers)
        
        # 计算使所有花园完善需要的花数量
        total_needed = sum(target - f for f in flowers)
        
        # 如果可以让所有花园完善
        if total_needed <= newFlowers:
            # 所有花园都完善
            all_full = full * n
            
            # 考虑n-1个花园完善，一个尽可能接近target-1
            remaining = newFlowers - (total_needed - (target - flowers[0]))
            max_min = min(target - 1, flowers[0] + remaining)
            almost_all_full = full * (n - 1) + partial * max_min
            
            return max(all_full, almost_all_full)
        
        # 初始化结果
        result = 0
        
        # 计算差分数组，用于快速计算填充成本
        diffs = [0] * n
        for i in range(n - 1):
            diffs[i] = flowers[i + 1] - flowers[i]
        
        # 从右向左枚举完善花园的数量
        complete_gardens = 0
        remain_flowers = newFlowers
        
        # 预先计算前缀和，用于快速计算填充成本
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + flowers[i]
        
        while complete_gardens <= n:
            # 计算当前未完善花园能达到的最大最小值
            if complete_gardens < n:
                incomplete = n - complete_gardens
                min_beauty = self.calculate_min_beauty(flowers, incomplete, remain_flowers, target, prefix_sum)
                result = max(result, full * complete_gardens + partial * min_beauty)
            
            # 尝试让下一个花园完善
            if complete_gardens < n:
                need = target - flowers[n - 1 - complete_gardens]
                if need > remain_flowers:
                    break
                remain_flowers -= need
                complete_gardens += 1
            else:
                break
        
        return result
    
    def calculate_min_beauty(self, flowers, incomplete, remain, target, prefix_sum):
        """使用二分查找高效计算未完善花园能达到的最大最小值"""
        if incomplete == 0:
            return 0
        
        # 如果所有未完善花园已经相同高度
        if flowers[0] == flowers[incomplete - 1]:
            can_fill = remain // incomplete
            return min(target - 1, flowers[0] + can_fill)
        
        # 二分查找能达到的最大最小值
        left, right = flowers[0], target - 1
        
        while left < right:
            mid = (left + right + 1) // 2
            
            # 计算使所有未完善花园达到mid高度需要的花数量
            # 优化：使用前缀和快速计算
            need = 0
            # 找到第一个大于等于mid的位置
            pos = self.binary_search(flowers, mid, incomplete)
            # 计算需要的花数量
            need = pos * mid - prefix_sum[pos]
            
            if need <= remain:
                left = mid
            else:
                right = mid - 1
        
        return left
    
    def binary_search(self, arr, target, end):
        """查找第一个大于等于target的位置"""
        left, right = 0, end - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumBeauty([1, 3, 1, 1], 7, 6, 12, 1))
