#User function Template for python3
class Solution:
	def NBitBinary(self, N):
	    ans = []
	    ones = zeros = 0
	    op = ""
	    
	    def generate(N, ones, zeros, op):
            if N == 0:
	            ans.append(op)
	            return
	   
	        generate(N-1, ones+1, zeros, op + '1')
	            
	        if ones > zeros:
	           
	            generate(N-1, ones, zeros+1, op + '0')
	            
	            
	    
	    generate(N, ones, zeros, op)
        return ans  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends