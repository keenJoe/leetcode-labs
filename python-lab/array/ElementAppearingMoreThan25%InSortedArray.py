# 1287. Element Appearing More Than 25% In Sorted Array

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        for i in range(length):
            if arr[i] == arr[i + length // 4]:
                return arr[i]
        return -1
    
    
    