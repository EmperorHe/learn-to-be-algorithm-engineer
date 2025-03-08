# 200.岛屿数量
"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      # 深度优先搜索，递归调用
      def dfs(grid, i, j):
        # 超过边界，类比于二叉树的到叶子结点的子节点
        if not isOver(grid, i, j):
          return
        
        # 不是岛屿，直接返回
        if grid[i][j] != '1':
          return
        
        # 将遍历过的结点值变为2
        grid[i][j] = '2'
        
        # 类比于二叉树遍历中的递归
        dfs(grid, i-1, j)
        dfs(grid, i+1, j)
        dfs(grid, i, j-1)
        dfs(grid, i, j+1)
        
        
      # 判断当前结点是否越界
      def isOver(grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

      count = 0
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          if grid[i][j] == '1':
            dfs(grid, i, j)
            count+=1
        
      return count
            