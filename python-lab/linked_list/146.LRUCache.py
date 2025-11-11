# 146. LRU Cache

'''
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

需要使用双向链表和哈希表来实现。

'''
# 定义一个双向链表的节点
from functools import cache
from platform import node


class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    # # 定义变量
    # lru_cache = {}
    # size = 0
    # capacity = 0
    # head = ListNode(0, 0)
    # tail = ListNode(0, 0)

    # 初始化 LRU 缓存
    def __init__(self, capacity: int):
        self.lru_cache = {}
        self.size = 0
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.lru_cache.get(key)
        if not node:
            return -1
        
        # 将当前节点移动到链表头
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.lru_cache.get(key)
        # 不存在
        if not node:
            new_node = ListNode(key, value)
            self.lru_cache[key] = new_node
            self.add_to_head(new_node)
            self.size += 1
            if self.size > self.capacity:
                # 删除链表尾节点
                tail_node = self.remove_tail()
                self.lru_cache.pop(tail_node.key)
                self.size -= 1
        else:
            node.value = value
            self.move_to_head(node)

    def add_to_head(self, node: ListNode):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def move_to_head(self, node: ListNode):
        # 先删除节点，即将当前节点的前后两个节点连接
        node.prev.next = node.next
        node.next.prev = node.prev

        # 再将节点添加到链表头
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self):
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node

    def remove_node(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)