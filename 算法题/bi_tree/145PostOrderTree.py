# 145.二叉树的后序遍历
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traversal(root, res)
        return res
        
    def traversal(self, node, res):
      if node == None:
        return
      
      # 左 右 中
      self.traversal(node.left, res)
      self.traversal(node.right, res)
      res.append(node.val)

    # 非递归实现
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中节点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]