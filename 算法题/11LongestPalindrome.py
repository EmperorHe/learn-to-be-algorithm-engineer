# 5.最长回文子串
# 给你一个字符串 s，找到 s 中最长的 回文子串。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 暴力解法 无法得出正确结果
        n = len(s)
        # 记录回文串的长度
        max_len = 0
        res = ""
        for i in range(n):
          start = i
          # 当前子回文串的长度
          cur_len = 0
          for j in range(n-1, i-1, -1):
            # 截取头字符和尾字符
            sub_i = s[i:i+1]
            sub_j = s[j:j+1]
            print("sub_i, sub_j:",sub_i, sub_j)
            if sub_i == sub_j:
              print("i,j:", i,j)
              if j>i:
                cur_len += 2
                i += 1
              elif j==i:
                cur_len += 1
                break
              else:
                break
            else:
              i = start
              cur_len = 0
              continue
          if cur_len > 0:
            if cur_len >= max_len:
              max_len = cur_len
              res = s[start:start+cur_len]

        return res
    
    def longestPalindrome2(self, s: str) -> str:
      # 与647题类似的解法
      # 1.dp[i][j] 表示下标i到j [i:j]的子串是否为回文串，True表示是，False表示不是
      # 2.dp推导式：if s[i] == s[j] and dp[i+1][j-1]: dp[i][j] = True
      #            elif s[i] == s[j] and j-i < 2: dp[i][j] = True
      #            else: dp[i][j] = False
      # 3.初始化 dp[i][i] = True
      # 4.遍历 从下到上，从左到右
      # 5.检查结果 找到最大的j-i+1
      
      n = len(s)
      dp = [[False for i in range(n)] for j in range(n)]
      for i in range(n):
        dp[i][i] = True
      
      for i in range(n-1, -1, -1):
        for j in range(i+1, n):
          if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
            dp[i][j] = True
          
      m = 0
      start = 0
      for i in range(n):
        for j in range(i, n):
          if dp[i][j] and j-i+1 > m:
            m = j-i+1
            start = i
            
      return s[start:start+m]
        
                
s = "aacabdkacaa"  
sl = Solution()
print(sl.longestPalindrome2(s))            
          