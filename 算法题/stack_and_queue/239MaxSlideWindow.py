# 239.滑动窗口最大值
"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
"""
from collections import deque
from typing import List

# 使用单调队列实现。
# 单调队列的定义：队列里的元素满足单调递减或递增的原则即可
# 这里使用自定义的单调队列，实现pop和push方法，返回单调队列里的队首元素(即最大值)

class MyQueue: # 单调递减队列
    def __init__(self):
        self.que = deque()

    def pop(self, val):
        # 如果元素等于单调队列的首元素，则进行弹出，否则表示之前push操作已经弹出了
        if self.que and self.que[0] == val:
            self.que.popleft()
        
    def push(self, val):
        # 判断插入单调队列的值是否大于队列的首元素，是则进行单调队列的维护(弹出小元素)
        # while self.que and val > self.que[0]:
        #     self.que.popleft()
        # self.que.append(val)

        #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
        #这样就保持了队列里的数值是单调从大到小的了。
        while self.que and val > self.que[-1]:
            self.que.pop() # 从队列后面弹出
        self.que.append(val)
        
    def front(self):
        # 只需要返回值即可，不要弹出队首元素
        return self.que[0]
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myQue = MyQueue()
        result = []
        for i in range(k):
          myQue.push(nums[i])
          
        result.append(myQue.front())
        
        for i in range(k, len(nums)):
            myQue.pop(nums[i - k]) #滑动窗口移除最前面元素
            myQue.push(nums[i]) #滑动窗口前加入最后面的元素
            result.append(myQue.front()) #记录对应的最大值
        return result
        
        
nums = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))