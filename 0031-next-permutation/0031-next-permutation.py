class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        i = n-2
        while i >= 0 :
            if arr[i] < arr[i+1]:
                break
            i -= 1
        if i < 0:
            arr.reverse()
        else:
            for j in range(n-1, i, -1):
                if arr[j] > arr[i]:
                    break
            arr[i], arr[j] = arr[j], arr[i]
            arr[i+1:] = reversed(arr[i+1:])
            
            
                
                
                
                
                