#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        prev = prev2 = 1
        curr = 0
        
        for i in range(2, n+1):
            curr = int((prev + prev2) % (1e9 + 7))
            prev2 = prev
            prev = curr
            
        
        return int(prev % (1e9 + 7))


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
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends