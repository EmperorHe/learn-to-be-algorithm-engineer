# Description: Reverse a singly linked list.
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        
        while node:
            # 保存下一个节点
            next_node = node.next
            # 反转指针
            node.next = prev
            # 更新prev和node
            prev = node
            node = next_node
            
        return prev