"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""

class Solution:
    def threeSum(self, nums):
        # 方法一：暴力尝试
        # res = list()
        # n = len(nums)
        # for i in range(n):
        #   for j in range(i+1, n):
        #     for k in range (j+1, n):
        #       if nums[i] + nums[j] + nums[k] == 0:
        #         curRes = [nums[i], nums[j], nums[k]]
        #         # 如何去除重复的数组，-> 由此得出，先排序
        #         res.append(curRes)
        
        # return res
        
        # 加上排序后暴力循环
        # nums.sort()
        # res = list()
        # n = len(nums)
        # for i in range(n-2):
        #   if i > 0 and nums[i] == nums[i - 1]:  # 避免重复
        #         continue
        #   for j in range(i+1, n):
        #     k = n-1
        #     while k > j:
        #       if nums[i] + nums[j] + nums[k] < 0:
        #         break
        #       if nums[i] + nums[j] + nums[k] == 0:
        #         curRes = [nums[i], nums[j], nums[k]]
        #         res.append(curRes)
        #         break
        #       k -= 1
        # return res   # 无法解决 [0,0,0,0]的重复结果问题
        
        nums.sort()  # 先排序
        res = []
        n = len(nums)

        for i in range(n - 2):  # 只需要遍历到倒数第三个
          if i > 0 and nums[i] == nums[i - 1]:  # 避免重复
            continue
          
          # 双指针进行遍历
          left, right = i + 1, n - 1
          while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
              res.append([nums[i], nums[left], nums[right]])

              # 去重：跳过相同的 `left` 和 `right`
              while left < right and nums[left] == nums[left + 1]:
                left += 1
              while left < right and nums[right] == nums[right - 1]:
                right -= 1

              left += 1
              right -= 1
            # 双指针进行移动
            elif total < 0:
              left += 1
            else:
              right -= 1
        return res




test1 = [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]
s = Solution()
print(s.threeSum(test1))