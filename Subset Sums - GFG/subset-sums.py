#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		ans = []
		ind = s = 0
		
		def generate(ind, s):
		    if ind == N:
		        ans.append(s)
		        return
		    
		    generate(ind+1, s+arr[ind])
		    
		    generate(ind+1, s)
		    
	    
	    generate(ind, s)
	    
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends