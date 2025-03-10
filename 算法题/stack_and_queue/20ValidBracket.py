# 20.有效的括号
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # 借用栈结构
        stack = []
        n = len(s)
        stack.append(s[0:1])
        # 使用字典
        d = {
          '(': ')',
          '[': ']',
          '{': '}'
        }
        for i in range(1, n):
          c = s[i:i+1]
          
          if len(stack) == 0: # 栈为空
            stack.append(c)
          else: # 栈不空
            if stack[-1] in d: # 当前元素在字典中
              if d[stack[-1]] == c: # 当前括号已匹配
                stack.pop()
              else:
                stack.append(c)
            else: # 不在字典说明不匹配
              return False
          
        return len(stack) == 0
      
s = "([])"
solution = Solution()
print(solution.isValid(s))