# 94.二叉树的中序遍历
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traversal(root, res)
        return res
      
    # 递归实现的逻辑思路
    # 1.确定 递归 函数的 参数 和 返回值 （前序遍历，结果保存在list中，参数为当前结点）
    # 2.确定 递归 的终止条件           （当遍历到空节点时表示遍历结束）
    # 3.确定单层 递归 的逻辑           （中序遍历 左 中 右）    
    def traversal(self, node, res):
      if node == None:
        return
      
      # 左 中 右
      self.traversal(node.left, res)
      res.append(node.val)
      self.traversal(node.right, res)
      
    # 非递归实现，用栈模拟
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []  # 不能提前将root节点加入stack中

        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树节点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左节点后处理栈顶节点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右节点
                cur = cur.right	
        return result