#User function Template for python3
import sys

class Solution:
    def minimumEnergy(self, height, n):
        
        dp = [-1] * (n)
        dp[0] = 0
        
        for i in range(1, n):
            
            left = abs(height[i] - height[i-1]) + dp[i-1]
            right = sys.maxsize
            
            if i > 1:
                right = abs(height[i] - height[i-2]) + dp[i-2]
            
            dp[i] = min(left, right)
        
        return dp[n-1]
        
        
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends