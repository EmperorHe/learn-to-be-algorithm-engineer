# 33.搜索旋转排序数组
"""
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 暴力循环
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == target:
        #         return i
        # return -1
      
        # 局部有序，二分查找
        low, high = 0, len(nums)-1
        while low <= high:
          mid = (low + high) // 2
          if nums[mid] == target:
                return mid
          # 左半边区域是有序的
          if nums[0] <= nums[mid]:
              # 目标值在左半边区域 
              if nums[0] <= target < nums[mid]:
                  high = mid - 1
              else:
                  low = mid + 1
          # 右半边区域是有序的
          else:
              # 目标值在右半边区域
              if nums[mid] < target <= nums[len(nums) - 1]:
                  low = mid + 1
              else:
                  high = mid - 1
        return -1

t = [4,5,6,7,0,1,2]
s = Solution()
print(s.search(t, 0))