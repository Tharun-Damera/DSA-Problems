import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxpro = 0
        minprice = sys.maxsize
        
        for i in range(n):
            minprice = min(minprice, prices[i])
            maxpro = max(maxpro, prices[i] - minprice)
                
        return maxpro
        
        