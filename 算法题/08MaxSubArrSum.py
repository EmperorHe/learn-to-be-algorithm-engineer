"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
"""

class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 1:
          return nums[0]
        
        temp = nums[0]
        res = nums[0]
        for i in range(1, n):
          # 动态规划思想：temp代表当前数组到下标i为止的最大值
          temp = max(temp + nums[i], nums[i])
          print("temp:",temp)
          res = max(temp, res)
      
        return res
          

s = Solution()
t = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(t)) 