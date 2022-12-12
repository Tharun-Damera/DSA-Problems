#User function Template for python3
import sys

class Solution:
    def minimumEnergy(self, height, n):
        
        prev = prev2 = 0
        
        for i in range(1, n):
            
            left = abs(height[i] - height[i-1]) + prev
            right = sys.maxsize
            
            if i > 1:
                right = abs(height[i] - height[i-2]) + prev2
            
            curr = min(left, right)
            prev2 = prev
            prev = curr
            
        
        return prev
        
        
    

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