"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 暴力解法： 转换成list数组，先反转，再插入链表中
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nums = list()
        node = head
        while(node):
          nums.append(node.val)
          node = node.next
        n = len(nums)
        loop = n // k
        for i in range(loop):
          self.reverseList(nums, i*k, (i+1)*k)
        
        print(nums)
        newHead = ListNode(-1)
        newNode = newHead
        for j in range(n):
          curNode = ListNode(nums[j])
          newNode.next = curNode
          newNode = newNode.next
        
        return newHead.next

    def reverseList(self, list, low, high):
        i = low
        j = high
        for k in range(i, j):
          if k < j:
            list[k], list[j-1] = list[j-1], list[k]
            j -= 1
          else:
            break
          
class Solution2:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
      # 创建虚拟头结点
      hair = ListNode(0)
      hair.next = head
      
      # 前一组的最后一个结点（相当于翻转链表的prev）
      pre = hair
      end = hair
      
      while end.next:
        for i in range(k):
          # 当前剩余结点不够k个，直接返回即可
          if not end:
            return hair.next
          end = end.next
        # end结点为None，那么循环结束
        if not end:
          break

        # start是当前组翻转中的第一个结点，next是下一组的起点
        start = pre.next
        next = end.next
        
        # 断开当前组最后的结点
        end.next = None
        pre.next = self.reverseNode(start)

        # 链接上翻转后的和原来断开的结点
        start.next = next
        pre, end = start, start
        
      
      return hair.next
      
    # 反转链表方法
    def reverseNode(self, head):
      prev = None
      node = head
      while node:
        # 保存下一个结点
        next_node = node.next
        # 反转指针
        node.next = prev
        prev = node
        node = next_node
      return prev

head = ListNode(1)
two = ListNode(2)
head.next = two
three = ListNode(3)
two.next = three
four = ListNode(4)
three.next = four
five = ListNode(5)
four.next = five

s = Solution2()
h = s.reverseKGroup(head, 3)
print(h)
