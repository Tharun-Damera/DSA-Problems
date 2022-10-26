#User function Template for python3

from typing import List

class Solution:
    
    def insertAtBottom(self, st, ele):
        if len(st) == 0:
            st.append(ele)
        else:
            tmp = st.pop()
            self.insertAtBottom(st, ele)
            st.append(tmp)
        
        
    def reverse(self,st): 
        
        if len(st) != 0:
            tmp = st.pop()
            self.reverse(st)
            self.insertAtBottom(st, tmp)
        
        return st


#{ 
 # Driver Code Starts
#Initial Template for Python 3

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            ans=(ob.reverse(arr))
            for el in ans:
                print(el,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends