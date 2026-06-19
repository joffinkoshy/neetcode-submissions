class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        ans=0

        for p in prices[1:]:
            buy=min(buy,p)
            ans=max(ans,p-buy)

        return ans
        