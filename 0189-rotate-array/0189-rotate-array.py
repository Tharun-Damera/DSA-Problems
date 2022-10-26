class Solution:
    
    def reverse(self, arr: List[int], i: int, j: int):
        left, right = i, j
        
        while left < right:
            
            arr[left], arr[right] = arr[right], arr[left]
            
            left += 1
            right -= 1
    
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr) 
        if n == 0 or n == 1 or k == 0 :
            return 
        if k > n:
            k = k % n
        
        self.reverse(arr, 0, n - k - 1)
        self.reverse(arr, n - k, n - 1)
        self.reverse(arr, 0, n - 1)
        
    
        
        
        