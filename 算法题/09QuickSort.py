# 912.手撕快排
"""
给你一个整数数组 nums，请你将该数组升序排列。
你必须在 不使用任何内置函数 的情况下解决问题，时间复杂度为 O(nlog(n))，并且空间复杂度尽可能小。

手撕快速排序
"""
import random
from typing import List  # 导入 List 类型

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return self.quickSort(nums, 0, n-1)
    
    
    def quickSort(self, nums, low, high):
        if low < high:
          # 分治的思想
          lt, gt = self.partition3(nums, low, high)
          self.quickSort(nums, low, lt-1)
          self.quickSort(nums, gt+1, high)
        return nums
        
        
    def partition(self, nums, low, high):
        random_int = random.randint(low, high)
        pivot = nums[random_int]
        # 将基准数和最后一个下标进行调换
        nums[high], nums[random_int] = nums[random_int], nums[high]
        
        i=low
        # 基于基准值放在high位置的 单指针法
        for j in range(low, high):
          if nums[j] < pivot:
            # 下标 i 均用来存储小于基准值的数
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        # 最终的i就表示小于基准值的个数
        
        nums[high], nums[i] = nums[i], nums[high]
        return i      
    
    def partition2(self, nums, low, high):
      pivot = nums[low]
      # 双指针法
      i = low+1
      j = high
      while True:
        while i <= j and nums[i] <= pivot:
          i += 1
        while i <= j and nums[j] > pivot:
          j -= 1
        
        if i>j:
          break
        
        nums[i], nums[j] = nums[j], nums[i]
      nums[low], nums[j] = nums[j], nums[low]  # 将基准值放到正确的位置
      return j  # 返回基准值的最终位置
    
    
    def partition3(self, nums, low, high):
      random_int = random.randint(low, high)
      pivot = nums[random_int]
      # 将基准数和最后一个下标进行调换
      nums[high], nums[random_int] = nums[random_int], nums[high]
      # 设置三分区，小于 [lt] 等于 [gt] 大于
      # 所有 lt<i<gt的元素都是等于当前pivot的值
      lt = low # 小于基准值的右边界
      gt = high# 大于基准值的左边界
      i = low # 一定要遍历到i>gt，也就是说要处理小于和等于情况下i的变化
      while i <= gt:
        if nums[i] < pivot:
            nums[i], nums[lt] = nums[lt], nums[i]
            lt += 1
            i += 1
        elif nums[i] > pivot:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
        else:
            i += 1
      return lt, gt
    
nums = [5,1,1,2,0,0]
s = Solution()
print(s.sortArray(nums))