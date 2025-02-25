# 2502. Design Memory Allocator

class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        pass

    '''
        size：连续内存块的大小
        mID：内存块的ID
        
        是不是需要记录连续内存块的开始和结束位置？
    '''
    def allocate(self, size: int, mID: int) -> int:
        n = len(self.memory)
        # 从左到右遍历，找到第一个连续的size大小的内存块
        for i in range(n):
            if self.memory[i] == 0:
                count += 1
                if count == size:
                    # 找到足够大的连续空间，将其分配给mID
                    for j in range(i - size + 1, i + 1):
                        self.memory[j] = mID
                    return i - size + 1
            else:
                count = 0
            # if self.memory[i] == 0:
            #     if i + size > n:
            #         return -1
            #     # 找到连续的size大小的内存块
            #     flag = True
            #     for j in range(i, i + size):
            #         if self.memory[j] != 0:
            #             flag = False
            #             break
            #     if flag:
            #         for k in range(i, i + size):
            #             self.memory[k] = mID
            #         return i
        return -1

    def freeMemory(self, mID: int) -> int:
        n = len(self.memory)
        count = 0
        for i in range(n):
            if self.memory[i] == mID:
                self.memory[i] = 0
                count += 1
        return count
    
    
    def allocate(self, size: int, mID: int) -> int:
        n = len(self.memory)
        count = 0  # 修复：添加count的初始化
        
        # 提前检查边界条件
        if size <= 0 or size > n:
            return -1
        
        # 从左到右遍历，找到第一个连续的size大小的内存块
        for i in range(n):
            if self.memory[i] == 0:
                count += 1
                if count == size:
                    start = i - size + 1
                    # 使用切片操作替代循环，提高效率
                    self.memory[start:i + 1] = [mID] * size
                    return start
            else:
                count = 0
        return -1
    
    def freeMemory(self, mID: int) -> int:
        # 使用列表推导式和sum优化计数过程
        count = sum(1 for i in range(len(self.memory)) if self.memory[i] == mID)
        # 使用列表推导式替换内存
        self.memory = [0 if x == mID else x for x in self.memory]
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)

if __name__ == "__main__":
    allocator = Allocator(10)
    print(allocator.allocate(3, 100))
    print(allocator.allocate(5, 101))
    print(allocator.freeMemory(100))
    print(allocator.allocate(5, 101))
    print(allocator.freeMemory(101))