class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def generate(stack = []):
            
            if len(stack) == 2 * n:
                if isValid(stack):
                    res.append("".join(stack))
                
            else:
                stack.append('(')
                generate(stack)
                stack.pop()
                stack.append(')')
                generate(stack)
                stack.pop()
        
        def isValid(arr):
            bal = 0
            for ch in arr:
                if ch == '(':
                    bal += 1
                else:
                    bal -= 1
                
                if bal < 0:
                    return False
            return bal == 0
    
        generate()
        return res
                