# 1206. Design Skiplist

import random


class Node:
    def __init__(self, val=-1, level=0):
        self.val = val                    # 节点值
        self.next = [None] * (level + 1)  # 每层的后继节点


class Skiplist:
    def __init__(self):
        self.max_level = 16              # 最大层数
        self.P = 0.5                     # 层数随机概率
        self.head = Node(-1, self.max_level)  # 头节点
        self.level = 0                   # 当前层数

    def search(self, target: int) -> bool:
        current = self.head
        # 从最高层开始查找
        for i in range(self.level, -1, -1):
            # 在当前层找到小于目标值的最大节点
            while current.next[i] and current.next[i].val < target:
                current = current.next[i]
        
        # 检查下一个节点是否为目标值
        current = current.next[0]
        return current is not None and current.val == target
        

    def add(self, num: int) -> None:
        # 记录每一层需要更新的节点
        update = [None] * (self.max_level + 1)
        current = self.head
        
        # 从最高层开始查找插入位置
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].val < num:
                current = current.next[i]
            update[i] = current
        
        # 随机生成新节点的层数
        new_level = self._random_level()
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level
        
        # 创建新节点并更新指针
        new_node = Node(num, new_level)
        for i in range(new_level + 1):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node
        

    def erase(self, num: int) -> bool:
        # 存储每层需要更新的节点
        update = [None] * (self.max_level + 1)
        current = self.head
        
        # 从最高层开始查找要删除的节点
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].val < num:
                current = current.next[i]
            update[i] = current
        
        # 获取要删除的节点
        current = current.next[0]
        
        # 如果节点不存在或值不匹配，返回False
        if not current or current.val != num:
            return False
        
        # 从下到上删除每层的节点引用
        for i in range(self.level + 1):
            if update[i].next[i] != current:
                break
            update[i].next[i] = current.next[i]
        
        # 更新跳表的当前最大层数
        while self.level > 0 and not self.head.next[self.level]:
            self.level -= 1
        
        return True
    
    def _random_level(self) -> int:
        level = 0
        while random.random() < self.P and level < self.max_level:
            level += 1
        return level
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)