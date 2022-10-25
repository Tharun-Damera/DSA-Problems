class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        num = -x if x < 0 else x
        
        while num != 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10
            
        rev = -rev if x < 0 else rev
        
        if rev in range(-2**31, 2**31):
            return rev
        else:
            return 0