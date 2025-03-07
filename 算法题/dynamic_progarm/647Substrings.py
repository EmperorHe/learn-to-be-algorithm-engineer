"""
647.回文子串
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
回文字符串 是正着读和倒过来读一样的字符串。
子字符串 是字符串中的由连续字符组成的一个序列。
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # 动态规划法
        # 1.dp[i][j] 表示下标i到j [i:j]的子串是否为回文串，True表示是，False表示不是
        # 2.dp推导式：if s[i] == s[j] and dp[i+1][j-1]: dp[i][j] = True
        #            elif s[i] == s[j] and i+1 > j-1: dp[i][j] = True
        #            else: dp[i][j] = False
        # 3.初始化 dp[i][i] = True
        # 4.遍历 从下到上，从左到右
        # 5.检查结果
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)] 
        # 记录回文串的个数
        res = 0
        
        for i in range(n):
          dp[i][i] = True
          res+=1
          
        for i in range(n-1, -1, -1):
          for j in range(i+1, n):
            if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]): 
              dp[i][j] = True
              res += 1
         
        return res              
      
      
t = "abab"
s = Solution()
print(s.countSubstrings(t))