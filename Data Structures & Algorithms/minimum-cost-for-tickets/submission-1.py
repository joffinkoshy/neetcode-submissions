from bisect import bisect_left
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        dp=[0]*(n+1)
        


        for i in range(n-1,-1,-1):

            # 1-day pass
            j=bisect_left(days,days[i]+1)
            one=costs[0]+dp[j]

            # 7-day pass

            j =bisect_left(days,days[i]+7)
            seven = costs[1] + dp[j]

            # 30-day pass

            j =bisect_left(days,days[i]+30)
            thirty = costs[2] + dp[j]

            dp[i]=min(one,seven,thirty)

        return dp[0]



        