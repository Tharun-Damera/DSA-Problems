#User function Template for python3

class Solution:
    def isSubsetSum (self, n, arr, k):
        
        dp = [[-1 for i in range(k+1)] for j in range(n+1)]
        def solve(arr, k, n):
            if k == 0:
                return True
            
            if n == 1:
                return arr[0] == k
                
            if dp[n][k] != -1:
                return dp[n][k]
            
            if arr[n-1] <= k:
                dp[n][k] = solve(arr, k-arr[n-1], n-1) or solve(arr, k, n-1)
                return dp[n][k]
            else:
                dp[n][k] = solve(arr, k, n-1)
                return dp[n][k]
        
        return solve(arr, sum, N)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends