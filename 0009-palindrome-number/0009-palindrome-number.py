class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= -2**31 and x <= 2**31-1:
            if x < 0:
                return False
            reverse = 0
            num = x
            while num != 0:
                digit = num % 10
                reverse = reverse * 10 + digit
                num //= 10
            
            return x == reverse
            
            