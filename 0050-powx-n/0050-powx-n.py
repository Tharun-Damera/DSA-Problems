class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = -n if n < 0 else n
        ans = 1.0
        
        while exp > 0:
            if exp % 2 == 0:
                x = x * x
                exp = exp // 2
            else:
                ans = ans * x
                exp -= 1
            
        
        if n < 0:
            return 1 / ans
        
        return ans