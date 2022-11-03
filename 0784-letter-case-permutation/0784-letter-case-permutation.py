class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def permute(ip, op):
            if len(ip) == 0:
                subs.append(op)
                return 
        
            if ip[0].isalpha():
                op1 = op + ip[0].lower()
                op2 = op + ip[0].upper()
                
                ip = ip[1:]
                permute(ip, op1)
                permute(ip, op2)
                return          
            
            else:
                op = op + ip[0]
                ip = ip[1:]
                
                permute(ip, op)
                return
                
        
        
        subs = []
        ip = s
        op = ""
        
        permute(ip, op)
        
        return subs