# 215. 数组中的第K个最大元素
"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""

from typing import List

### 基于快排的思路，找到第k大的元素，就是找到第n-k小的元素
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        return self.quickSelect(nums, 0, n - 1, target)
    
    def quickSelect(self, nums, low, high, target):
        if low < high:
            pi = self.partition(nums, low, high)
            if pi == target:
                return nums[pi]
            elif pi < target:
                return self.quickSelect(nums, pi + 1, high, target)
            else:
                return self.quickSelect(nums, low, pi - 1, target)
        return nums[low]
    
    def partition(self, nums, low, high):
        # 通过单指针找到基准值的位置
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j]<pivot:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
        # 通过双指针找到基准值的位置
        # pivot = nums[low]  # 选择第一个元素作为基准值
        # i = low + 1
        # j = high
        # while True:
        #     while i < j and nums[i] <= pivot:  # 从左向右找第一个大于 pivot 的元素
        #         i += 1
        #     while i < j and nums[j] > pivot:  # 从右向左找第一个小于等于 pivot 的元素
        #         j -= 1
        #     if i >= j:
        #         break
        #     nums[i], nums[j] = nums[j], nums[i]  # 交换这两个元素
        # nums[low], nums[j] = nums[j], nums[low]  # 将基准值放到正确的位置
        # return j

nums = [7,6,5,4,3,2,1]
k = 2
solution = Solution()
print(f"第{k}大的元素:", solution.findKthLargest(nums, k))

"""
以上方法会超出时间限制，主要问题为：存在较多相同元素时，会导致递归深度过大
对快排进行三路分区，将相同元素分到中间，减少递归深度
"""
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        return self.quickSelect(nums, 0, n - 1, target)
    
    def quickSelect(self, nums, low, high, target):
        if low < high:
            lt, gt = self.partition(nums, low, high)
            if target < lt:  # 目标在小于基准值的部分
                return self.quickSelect(nums, low, lt - 1, target)
            elif target > gt:  # 目标在大于基准值的部分
                return self.quickSelect(nums, gt + 1, high, target)
            else:  # 目标在等于基准值的部分（重复元素部分）
                return nums[target]
        return nums[low]
    
    def partition(self, nums, low, high):
        # 随机选择一个基准值
        pivot_index = random.randint(low, high)
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
        pivot = nums[high]
        lt = low  # 小于基准值的右边界
        gt = high  # 大于基准值的左边界
        i = low
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
        
        
def quickSortSelf(arr, low, high):
    if low < high:
        pi = partitionDS(arr, low, high)
        quickSortSelf(arr, low, pi - 1)
        quickSortSelf(arr, pi + 1, high)
        
def partitionSelf(arr, low, high):
    # pivot = arr[low]
    # i = low
    # j = high
    # while i < j:
    #     while i < j and arr[j] > pivot:
    #         j -= 1
    #     while i < j and arr[i] <= pivot:
    #         i += 1
    #     if i < j:
    #         arr[i], arr[j] = arr[j], arr[i]
    # arr[low], arr[i] = arr[i], arr[low]
    # return i
    pivot = arr[low]  # 选择第一个元素作为基准值
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:  # 从左向右找第一个大于 pivot 的元素
            i += 1
        while i <= j and arr[j] > pivot:  # 从右向左找第一个小于等于 pivot 的元素
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]  # 交换这两个元素
    arr[low], arr[j] = arr[j], arr[low]  # 将基准值放到正确的位置
    return j  # 返回基准值的最终位置
  
def partitionDS(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i