class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        ele = -1
        
        for i in range(n):
            if cnt == 0:
                ele = nums[i]
                
            if ele == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                
        return ele
        