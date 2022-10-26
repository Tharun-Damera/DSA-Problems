class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        if n == 0:
            return

        k = 0
        while k < n:
            if arr[k] == 0:
                break
            else: 
                k+= 1
        
        i, j = k, k + 1
        while i < n and j < n:
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1