# 460. LFU Cache

'''
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：

LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。
为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。

当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。

函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

最不经常使用：可以使用双向链表来实现，链表的节点按照使用计数器排序，使用计数器最小的节点在最前面。
最久未使用：可以使用双向链表来实现，链表的节点按照插入时间排序，插入时间最久的节点在最前面。

如果两个节点的使用次数相同，那么排序时需要考虑插入时间问题。

使用计数器最小的节点在最前面。
插入时间最久的节点在最前面。

要基于双向链表实现，使用哈希表存储 key 和节点
节点包括：value next prev count
LFUCache 结构设计：
1、哈希表
2、capacity
3、head
4、tail
'''

# class ListNode:
#     def __init__(self, key: int, value: int):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#         self.count = 1

# class LFUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.capacity = capacity
#         self.head = ListNode(0, 0)
#         self.tail = ListNode(0, 0)
#         self.head.next = self.tail
#         self.tail.prev = self.head
       

#     def get(self, key: int) -> int:
#         node = self.cache.get(key)
#         if not node:
#             return -1

#         # 更新节点的计数器+1
#         self.update_count(node)
#         # 将当前节点移动到链表头
#         self.move_to_correct_position(node)
#         return node.value

#     # get 时候会更新使用频率和时间
#     # put 时候会删除节点
#     # 如果节点存在，则更新节点值，并移动到链表头，更新计数器
#     # 如果节点不存在，则创建新节点，并插入到链表头，更新计数器
#     # 如果缓存达到容量，则删除最不经常使用的节点，并插入新节点
#     # 如何找到最不经常使用的节点？
#     def put(self, key: int, value: int) -> None:
#         if self.capacity == 0:
#             return

#         node = self.cache.get(key)
#         if node:
#             node.value = value
#             self.update_count(node)
#             self.move_to_correct_position(node)
#         else:
#             # 缓存达到容量，需要删除最不经常使用的节点
#             if len(self.cache) >= self.capacity:
#                 self.remove_least_frequent_node()

#             new_node = ListNode(key, value)
#             self.cache[key] = new_node
#             # 最新的节点，需要移动到链表的头部
#             self.move_to_correct_position(new_node)


#     def remove_least_frequent_node(self) -> None:
#         # head.next 就是 count 最小且最久未使用的节点
#         to_remove = self.head.next
        
#         # 从链表中删除
#         self.head.next = to_remove.next
#         to_remove.next.prev = self.head
    
#         # 从哈希表中删除
#         del self.cache[to_remove.key]
        
#     # 将当前节点移动到正确的位置
#     # 先删除节点：删除即将当前节点和其前后两个节点断开，将其前后两个节点连起来
#     # 再将当前节点插入到表头：将当前节点插入到 head 之后，并更新 head 和 head.next 两个节点的相关指针信息
#     def move_to_correct_position(self, node: ListNode) -> None:
#         # 如果节点已在链表中，先删除
#         if node.prev is not None:
#             node.prev.next = node.next
#             node.next.prev = node.prev
        
#         # 从 head 开始找合适的位置
#         curr = self.head.next
#         while curr != self.tail:
#             # 找到第一个 count 大于当前节点的位置
#             if curr.count > node.count:
#                 break
#             curr = curr.next
        
#         # 插入到 curr 之前
#         node.prev = curr.prev
#         node.next = curr
#         curr.prev.next = node
#         curr.prev = node

#     def update_count(self, node: ListNode) -> None:
#         node.count += 1

#     def remove_node(self, node: ListNode) -> None:
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         node.prev = None
#         node.next = None
#         del self.cache[node.key]

from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add_to_head(self, node):
        """在头部添加节点"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove(self, node):
        """删除指定节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_tail(self):
        """删除尾部节点（最久未使用）"""
        if self.size > 0:
            tail_node = self.tail.prev
            self.remove(tail_node)
            return tail_node
        return None
    
    def is_empty(self):
        return self.size == 0

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}  # key -> Node
        self.freq_to_list = defaultdict(DoubleLinkedList)  # freq -> DLL
    
    def _update_freq(self, node):
        """更新节点频率"""
        freq = node.freq
        
        # 从旧频率链表中删除
        self.freq_to_list[freq].remove(node)
        
        # 如果旧频率链表为空且是最小频率，更新 min_freq
        if self.freq_to_list[freq].is_empty() and freq == self.min_freq:
            self.min_freq += 1
        
        # 频率+1，加入新频率链表头部
        node.freq += 1
        self.freq_to_list[node.freq].add_to_head(node)
    
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._update_freq(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            # 更新现有节点
            node = self.key_to_node[key]
            node.value = value
            self._update_freq(node)
        else:
            # 插入新节点
            if len(self.key_to_node) >= self.capacity:
                # 删除最小频率链表的尾部节点（最久未使用）
                min_freq_list = self.freq_to_list[self.min_freq]
                to_remove = min_freq_list.remove_tail()
                del self.key_to_node[to_remove.key]
            
            # 创建新节点
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.freq_to_list[1].add_to_head(new_node)
            self.min_freq = 1  # 新节点频率为1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)