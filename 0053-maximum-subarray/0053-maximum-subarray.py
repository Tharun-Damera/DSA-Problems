import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        maxSum = ~sys.maxsize
        curSum = 0
        s = 0
        for i in range(n):
            curSum += nums[i]
            if curSum > maxSum:
                maxSum = curSum
                si = s
                ei = i
            if curSum < 0:
                curSum = 0
                s = i + 1
        
        return maxSum