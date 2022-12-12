#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		
		prev = arr[0]
		prev2 = 0
		
		
		for i in range(1, n):
		    pick = arr[i]
		    if i > 1:
		        pick += prev2
		        
		    notPick = 0 + prev
		    
		    curr = max(pick, notPick)
		    prev2 = prev
		    prev = curr
		   
		return prev
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends