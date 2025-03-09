# 2070. Most Beautiful Item for Each Query

'''
    1、先对items进行排序，按照价格升序排序，如果价格相同，则按照美丽值降序排序；
    2、遍历queries，对于每个query，使用二分查找，找到价格大于等于query的价格的最大美丽值，然后返回美丽值；
    3、如果找不到，则返回0；
    4、返回结果。
'''

from typing import List


class Solution:
    # def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    #     items.sort(key=lambda x: (x[0], -x[1]))
    #     for i in range(len(items)):
    #         items[i].append(i)

    #     queries.sort()
    #     result = []
    #     for query in queries:
    #         max_beauty = self.find_max_beauty(items, query)
    #         result.append(max_beauty)
    #     return result
    
    # def find_max_beauty(self, items: List[List[int]], query: int) -> int:
    #     left, right = 0, len(items) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if items[mid][0] <= query:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return items[right][1]

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # 按价格排序，并预处理每个价格点的最大美丽值
        items.sort()  # 按价格排序
        n = len(items)
        
        # 更新每个价格点的最大美丽值，确保每个价格点都保存了不超过该价格的最大美丽值，这样我们只需要找到不超过查询价格的最后一个物品，其美丽值就是答案
        for i in range(1, n):
            if items[i][1] < items[i-1][1]:
                items[i][1] = items[i-1][1]
        
        result = []
        for query in queries:
            result.append(self.find_max_beauty(items, query))
        
        return result

    def find_max_beauty(self, items: List[List[int]], query: int) -> int:
        # 如果没有物品或查询价格小于最小价格，返回0
        if not items or query < items[0][0]:
            return 0
            
        # 二分查找找到价格不超过query的最后一个物品
        left, right = 0, len(items) - 1
        while left <= right:
            mid = (left + right) // 2
            if items[mid][0] <= query:
                left = mid + 1
            else:
                right = mid - 1
        
        # 如果没有找到符合条件的物品，返回0
        if right < 0:
            return 0
        
        # 由于我们已经预处理了每个价格点的最大美丽值，直接返回
        return items[right][1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]))
