class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opened = closed = n
        params = []
        op = ""
        
        def generate(opened, closed, op):
            if opened == 0 and closed == 0:
                params.append(op)
                return
            
            if opened != 0:
                generate(opened-1, closed, op + '(')
                
            if opened < closed:                    
                generate(opened, closed-1, op + ')')
            
            return
        
        
        
        generate(opened, closed, op)
        return params
                