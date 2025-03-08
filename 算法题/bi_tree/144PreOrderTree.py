# 144.二叉树的前序遍历
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traversal(root, res)
        return res
    
    # 递归实现的逻辑思路
    # 1.确定 递归 函数的 参数 和 返回值 （前序遍历，结果保存在list中，参数为当前结点）
    # 2.确定 递归 的终止条件           （当遍历到空节点时表示遍历结束）
    # 3.确定单层 递归 的逻辑           （前序遍历 中 -> 左 -> 右）    
    def traversal(self, node: TreeNode, res: List[int]):
        if node == None:
            return
        
        res.append(node.val)
        self.traversal(node.left, res)
        self.traversal(node.right, res)
        
        
    
    # 非递归实现，使用栈结构和迭代法
    # 1.将根节点压入栈，随后弹出。
    # 2.再分别压入右子结点，左子节点。
    # 3.弹出左子节点，压入对应的 “右子节点，左子结点”
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            # 先取出父节点
            node = stack.pop()
            result.append(node.val)
            
            # 再压入右子节点
            if node.right:
                stack.append(node.right)
            
            # 在压入左子结点
            if node.left:
                stack.append(node.left)
        
        return result
    