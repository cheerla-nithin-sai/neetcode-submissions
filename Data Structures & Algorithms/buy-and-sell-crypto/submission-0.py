class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        mm=0
        for buy in range(len(prices)):
            for sell in range(buy,len(prices)):
                m=max(m,prices[sell]-prices[buy])
            mm=max(mm,m)
        return mm
        
        