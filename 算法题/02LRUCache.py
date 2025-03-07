"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
"""



# 解法：哈希表 + 双向链表
# 思路：
# 1.哈希表：存储key和value
# 2.双向链表：存储key和访问次数，按照访问次数排序，最近访问的在链表头，最久访问的在链表尾
# 3.每次访问一个key，通过哈希表找到key，然后将其从链表中删除，再插入到链表头
# 4.当插入一个key时，如果容量已满，则删除链表尾部的key，然后将其插入到链表头

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            self.addToHead(node)
            if self.size > self.capacity:
                ### 删除链表尾部的key，当key为0时，会报错
                # print('tail.key:', self.tail.prev.key)
                remove_node = self.removeTail()
                self.cache.pop(remove_node.key)
        
    ### 使用key进行删除节点，没有维护到head和tail的key值
    # def remove_node(self, key: int) -> None:
    #     node = self.cache[key]
    #     node.prev.next = node.next
    #     node.next.prev = node.prev
    #     self.size -= 1
        
    # def add_head(self, key: int, value: int) -> None:
    #     node = DLinkedNode(key, value)
    #     node.prev = self.head
    #     node.next = self.head.next
    #     self.size += 1
    
    
    def removeNode(self, node: DLinkedNode):
      node.prev.next = node.next
      node.next.prev = node.prev
      self.size -= 1
      
    def moveToHead(self, node: DLinkedNode):
      self.removeNode(node)
      self.addToHead(node)
      
    def removeTail(self):
      node = self.tail.prev
      self.removeNode(node)
      return node   
    
    def addToHead(self, node: DLinkedNode):
      node.prev = self.head
      node.next = self.head.next
      self.head.next.prev = node
      self.head.next = node
      self.size += 1
        
# 测试
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 返回 1
cache.put(3, 3)  # 移除 key 2
print(cache.get(2))  # 返回 -1
cache.put(4, 4)  # 移除 key 1
print(cache.get(1))  # 返回 -1

