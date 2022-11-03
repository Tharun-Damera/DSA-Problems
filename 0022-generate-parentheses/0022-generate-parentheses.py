class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opened = closed = n
        params = []
        op = ""
        
        def generate(opened, closed, op):
            if opened == 0 and closed == 0:
                params.append(op)
                return
            
            if opened == closed:
                generate(opened-1, closed, op + '(')
                
            elif opened < closed:
                if opened == 0:
                    generate(opened, closed-1, op + ')')
                
                else:
                    generate(opened-1, closed, op + '(')
                    
                    generate(opened, closed-1, op + ')')
            
            return
        
        
        
        generate(opened, closed, op)
        return params
                