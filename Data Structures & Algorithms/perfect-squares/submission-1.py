class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        dp[1]=1

        i=1
        squares=[]

        while i*i<=n:
            squares.append(i*i)
            dp[i*i]=1
            i+=1

        for i in range(1,n+1):
            for sq in squares:
                if sq>i:
                    break

                dp[i]=min(dp[i],dp[i-sq]+1)

        return dp[n]

