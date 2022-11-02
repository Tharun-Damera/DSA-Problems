class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def generateSubsets(ip, op):
            if len(ip) == 0:
                subs.add(tuple(sorted(op)))
                return
        
            op1 = op.copy()
            op2 = op.copy()
            op2.append(ip[0])
            del ip[0]
            
            small_ip = ip.copy()
            
            generateSubsets(ip, op1)
            
            generateSubsets(small_ip, op2)
            
            return
        
        subs = set()
        op = []
        generateSubsets(nums, op)
        
        return subs