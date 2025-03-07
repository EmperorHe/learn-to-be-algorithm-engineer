"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力解法
        # n = len(nums)
        # for i in range(n):
        #   for j in range(i+1, n):
        #     if nums[i] + nums[j] == target:
        #       return [i, j]
        
        # 因为题目给出，每种输入只会对应一个答案，于是考虑使用哈希表键值对匹配target
        # [2,7,11,15] ==> {2:0, 7:1, 11:2, 15:3}
        # 寻找结果为9  ==> {9-2=7， 9-7=2}
        hash = {}
        for i in range(len(nums)):
          if target - nums[i] in hash:
            return [i, hash[target - nums[i]]]
          else:
            hash[nums[i]] = i
        
        return []
            

case1 = [2,7,11,15]
target = 26
s = Solution()
print(s.twoSum(case1, target))