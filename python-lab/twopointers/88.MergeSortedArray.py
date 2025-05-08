# 88. Merge Sorted Array

"""
示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
示例 3：

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

"""


from typing import List


class Solution:
    # 从后向前遍历，将nums2的元素插入到nums1的末尾
    # 这个非常重要！！！
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 初始化三个指针
        p1 = m - 1  # nums1的有效元素指针
        p2 = n - 1  # nums2的指针
        p = m + n - 1  # 合并后的数组指针
        
        # 从后向前遍历
        while p2 >= 0:  # 只要nums2还有元素需要处理
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                # 如果nums1的元素更大，将其移动到末尾
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # 如果nums2的元素更大或相等，将nums2的元素放入
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)