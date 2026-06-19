class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        ans=0

        for p in prices[1:]:
            if p<buy:
                buy=p
            else:
                ans=max(ans,p-buy)

        return ans
        