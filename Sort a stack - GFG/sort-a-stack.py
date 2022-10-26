class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    
    def insertInOrder(self, s, ele):
        if len(s) == 0 or ele > s[-1]:
            s.append(ele)
            return
        else:
            tmp = s.pop()
            self.insertInOrder(s, ele)
            s.append(tmp)
            
    
    def sorted(self, s):
        if len(s) != 0:
            tmp = s.pop()
            self.sorted(s)
            self.insertInOrder(s, tmp)



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends