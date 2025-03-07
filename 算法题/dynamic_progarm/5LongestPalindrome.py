# 5.最长回文子串
# 给你一个字符串 s，找到 s 中最长的 回文子串。
class Solution:
  def longestPalindrome(self, s: str) -> str:
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
print(sl.longestPalindrome(s))  