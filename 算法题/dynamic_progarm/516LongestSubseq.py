"""
516.最长回文子序列
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 动态规划方法
        # 1.dp[i][j] 表示 下标从i到j s[i:j]的子串中最长的子序列的长度
        # 2.if i == j: dp[i][j] = dp[i+1][j-1] + 2
        #   else dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # 3.初始化 dp[i][i] = 1
        # 4.遍历 从左往右，从下往上
        # 5.检查结果
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
          dp[i][i] = 1
        
        # 从下往上，从左往右
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
      
t = "bbbab"
s = Solution()
print(s.longestPalindromeSubseq(t))