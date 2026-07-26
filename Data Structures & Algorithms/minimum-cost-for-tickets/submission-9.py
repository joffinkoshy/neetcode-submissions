from bisect import bisect_left

class Solution:
    def mincostTickets(self, days, costs):
        n = len(days)
        
        dp = [0] * (n + 1)

        durations = [1, 7, 30]

        for i in range(n - 1, -1, -1):
            dp[i] = float('inf')

            for duration, cost in zip(durations, costs):
                j = bisect_left(days, days[i] + duration)
                dp[i] = min(dp[i], cost + dp[j])

        return dp[0]