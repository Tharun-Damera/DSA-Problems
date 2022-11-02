class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def generateAllSubsets(ip, op): 
            if len(ip) == 0:
                subs.append(op)
                return
            
            o1 = op.copy()
            o2 = op.copy()
            o2.append(ip[0])
            del ip[0]
            
            sip = ip.copy()
            print(ip)
            generateAllSubsets(ip, o1)
            print(sip)
            generateAllSubsets(sip, o2)
            
            return                   
        
        
        subs = []
        op = []
        generateAllSubsets(nums, op)
        
        return subs
        
        