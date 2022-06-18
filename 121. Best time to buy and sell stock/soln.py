"""
Sliding window 
Two pointer
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        lp,rp = 0,0
        while rp<len(prices):
            profit = max(profit, prices[rp]-prices[lp])
            if prices[lp]>prices[rp]:
                lp +=1
            else:
                rp +=1
        return profit