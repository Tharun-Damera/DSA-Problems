#User function Template for python3

class Solution:
    def safePos(self, n, k):
        if n == 1:
            return 1
            
        ans = [i for i in range(1, n+1)]
        index = 0
        k -= 1
        def alive(n, k, index):
            if n == 1:
                return
            
            index = (index + k) % n
            del ans[index]
            alive(len(ans), k, index)
            
        alive(n, k, index)
        return ans[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,k=map(int,input().split())
        
        ob = Solution()
        print(ob.safePos(n,k))
# } Driver Code Ends