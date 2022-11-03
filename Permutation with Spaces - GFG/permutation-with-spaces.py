#User function Template for python3

class Solution:
    def permutation (self, S):
        
        def pSpaces(ip, op):
            if len(ip) == 0:
                strings.append(op)
                return
            
            op1 = op + " " + ip[0]
            op2 = op + ip[0]
            
            ip = ip[1:]
            sip = ip
            pSpaces(ip, op1)
            pSpaces(sip, op2)
            return 
        
        ip = S
        op = ip[0]
        ip = ip[1:]
        strings = []
        pSpaces(ip, op)
        
        return strings
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends