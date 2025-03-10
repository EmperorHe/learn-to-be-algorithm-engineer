# 300.最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 动态规划
        # 1.定义dp数组，dp[i]表示到下标i为止的数组中最长递增子序列的长度
        # 2.状态转移方程，dp[i] = dp[i-1] + 1 if nums[i] > nums[i-1] else dp[i-1]
        
        # 状态转移方程设计有问题，实际应该为：dp[i] = max(dp[j]) + 1 其中0≤j<i 且 nums[j]<nums[i]
        # 也就是说，数组[0,j]内有一个数小于nums[i]，则dp[i] = man(dp[j]) + 1
        # 3.初始化，dp[0] = 1
        # 4.遍历，从左往右
        # 5.检查
        if not nums:
            return 0
        dp = []
        for i in range(n):
            # 没一个元素dp[i]都初始化为 1 
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

          