class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        if n == 0 or n == 1:
            return 
        
        lo, mid, hi = 0, 0, n-1
        
        while mid <= hi:
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo += 1
                mid += 1
                
            elif arr[mid] == 1:
                mid += 1
            
            else:
                arr[hi], arr[mid] = arr[mid], arr[hi]
                hi -= 1
        
                
            
            
            
            
            
            