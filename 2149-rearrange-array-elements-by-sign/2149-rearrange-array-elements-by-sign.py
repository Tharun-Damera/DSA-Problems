class Solution:
    def rearrangeArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n in range(2, 2*10**5+1):
            res = [-1] * n
            pos = 0
            neg = 1
            for i in range(n):
                if arr[i] >= 0:
                    res[pos] = arr[i]
                    pos += 2
                else:
                    res[neg] = arr[i]
                    neg += 2
                
        return res
        
                    
                    
                    
                    
            