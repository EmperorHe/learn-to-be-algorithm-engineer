# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        max_len = 0
        char_set = set()
        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            else:
                char_set.add(s[j])
                max_len = max(max_len, j - i + 1)
        
        return max_len
            
            
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(""))
    

"""
思路：双指针法 加 set集合
"""
    
    
# def length_of_longest_substring(s: str) -> int:
#     char_set = set()
#     left = 0  # 左指针
#     max_len = 0  # 记录最长子串的长度

#     for right in range(len(s)):  # 右指针遍历字符串
#         while s[right] in char_set:
#             char_set.remove(s[left])  # 删除左指针字符
#             left += 1  # 左指针右移
        
#         char_set.add(s[right])  # 加入右指针字符
#         max_len = max(max_len, right - left + 1)  # 更新最大长度

#     return max_len

# # 测试
# s = "abcabcbb"
# print(length_of_longest_substring(s))  # 输出: 3