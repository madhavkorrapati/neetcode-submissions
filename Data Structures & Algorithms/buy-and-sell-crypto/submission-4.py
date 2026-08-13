class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        min_n=prices[0]
        r=0
        while r<len(prices):
            if min_n>prices[r]:
                min_n=prices[r]
            if prices[r]-min_n> l:
                l=prices[r]-min_n
            r+=1
        return l

            