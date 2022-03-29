class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Resoning
        - Kadane algorithm
        
        '''
        bs = 0
        cs = 0
        for i in range(len(prices)-1):
            cs = max(0, cs + prices[i+1] - prices[i])
            bs = max(bs, cs)
        return bs
