# 堆排序

# 堆排序
class MaxHeap:
    """大根堆实现"""
    
    def __init__(self, arr=None):
        """初始化大根堆"""
        self.heap = []
        if arr:
            self.heap = arr[:]
            self.build_max_heap()
    
    def parent(self, i):
        """获取父节点索引"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """获取左子节点索引"""
        return 2 * i + 1
    
    def right_child(self, i):
        """获取右子节点索引"""
        return 2 * i + 2
    
    def max_heapify(self, i):
        """维护大根堆性质"""
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        # 找到父节点和子节点中最大的元素
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        # 如果最大元素不是父节点，则交换并递归调整
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    
    def build_max_heap(self):
        """将无序数组转换为大根堆"""
        # 从最后一个非叶子节点开始，向上调整
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.max_heapify(i)
    
    def insert(self, value):
        """插入新元素"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i):
        """向上调整（用于插入操作）"""
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            parent_idx = self.parent(i)
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx
    
    def extract_max(self):
        """提取并删除最大元素"""
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # 保存最大值
        max_val = self.heap[0]
        # 将最后一个元素移到根部
        self.heap[0] = self.heap.pop()
        # 重新调整堆
        self.max_heapify(0)
        
        return max_val
    
    def get_max(self):
        """获取最大元素（不删除）"""
        return self.heap[0] if self.heap else None
    
    def get_top_k_elements(self, k):
        """获取前K个最大的元素"""
        if k <= 0:
            return []
        
        if k >= len(self.heap):
            # 如果k大于等于堆大小，返回整个堆的排序结果
            return self.heap_sort()
        
        # 创建堆的副本，避免破坏原堆
        temp_heap = MaxHeap(self.heap)
        result = []
        
        for _ in range(k):
            max_val = temp_heap.extract_max()
            if max_val is not None:
                result.append(max_val)
        
        return result
    
    def heap_sort(self):
        """堆排序 - 返回降序排列的数组"""
        # 创建副本避免破坏原堆
        temp_heap = MaxHeap(self.heap)
        result = []
        
        while temp_heap.heap:
            result.append(temp_heap.extract_max())
        
        return result
    
    def size(self):
        """返回堆的大小"""
        return len(self.heap)
    
    def is_empty(self):
        """检查堆是否为空"""
        return len(self.heap) == 0
    
    def display(self):
        """显示堆的内容"""
        return self.heap


def demo():
    """演示大根堆的使用"""
    print("=== 大根堆演示 ===")
    
    # 测试数据
    arr = [4, 10, 3, 5, 1, 15, 9, 2, 6, 11]
    print(f"原始数组: {arr}")
    
    # Step 1: 创建大根堆
    print("\nStep 1: 创建大根堆")
    max_heap = MaxHeap(arr)
    print(f"大根堆: {max_heap.display()}")
    print(f"最大元素: {max_heap.get_max()}")
    
    # Step 2: 获取前K个最大元素
    print("\nStep 2: 获取前K个最大元素")
    k = 3
    top_k = max_heap.get_top_k_elements(k)
    print(f"前{k}个最大元素: {top_k}")
    
    k = 5
    top_k = max_heap.get_top_k_elements(k)
    print(f"前{k}个最大元素: {top_k}")
    
    # Step 3: 插入新元素
    print("\nStep 3: 插入新元素")
    new_val = 20
    max_heap.insert(new_val)
    print(f"插入{new_val}后的堆: {max_heap.display()}")
    print(f"新的最大元素: {max_heap.get_max()}")
    
    # Step 4: 提取最大元素
    print("\nStep 4: 提取最大元素")
    max_val = max_heap.extract_max()
    print(f"提取的最大元素: {max_val}")
    print(f"提取后的堆: {max_heap.display()}")
    
    # Step 5: 完整的堆排序
    print("\nStep 5: 堆排序结果")
    sorted_arr = max_heap.heap_sort()
    print(f"降序排列: {sorted_arr}")


if __name__ == "__main__":
    demo()