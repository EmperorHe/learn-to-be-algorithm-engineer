#将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        node1 = list1
        node2 = list2
        res = ListNode(0)
        cur = res
        
        while node1 and node2:
          if(node1.val < node2.val):
            cur.next = node1
            node1 = node1.next
          else:
            cur.next = node2
            node2 = node2.next
          cur = cur.next
        
        if node1:
            cur.next = node1
    
        if node2:
            cur.next = node2
        
        return res.next
      
      
s = Solution()
h1 = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
h5 = ListNode(5)
h1.next = h2
h2.next = h3
h3.next = h4
h4.next = h5

k1 = ListNode(1)
k2 = ListNode(2)
k3 = ListNode(3)
k4 = ListNode(4)
k5 = ListNode(5)
k1.next = k2
k2.next = k3
k3.next = k4
k4.next = k5


print(s.mergeTwoLists(h1, k1))