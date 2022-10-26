class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n

        t1, t2 = 0, 1
        while t2 < n:
            if nums[t1] != nums[t2] :
                t1 += 1
                nums[t1] = nums[t2]
            t2 += 1
        return t1 + 1