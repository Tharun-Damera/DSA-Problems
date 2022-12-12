#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        prev = a[0]
		prev2 = 0
		
		
		for i in range(1, n):
		    pick = a[i]
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
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends