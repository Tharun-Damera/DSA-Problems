class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ksum = 0
        cnt = 0
        d = dict()
        d[0] = 1
        
        for i in range(n):
            ksum += nums[i]
            
            if ksum - k in d:
                cnt += d[ksum - k]
            
            d[ksum] = d.get(ksum, 0) + 1
            
        return cnt
                