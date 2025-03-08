# 102.二叉树的层序遍历
# Definition for a binary tree node.
from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
          return []
        #使用队列 1.queue.Queue 2.collections.deque 3.list的append和pop(0)方法
        q = deque([root])
        result = []
        while q:
          size = len(q)
          # 存储遍历当前层的结点
          level = []
          while size > 0:
            node = q.popleft()
            level.append(node.val)
            if node.left:
              q.append(node.left)
            if node.right:
              q.append(node.right)
            size -= 1

          result.append(level)
        
        return result