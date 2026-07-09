class Solution:
    def tribonacci(self, n: int) -> int:
        memo={
            0:0,
            1:1,
            2:1
        }

        if n<=2:
            return memo[n]

        def fib(x):
            if x in memo:
                return memo[x]

            memo[x]=fib(x-1)+fib(x-2)+fib(x-3)

            return memo[x]

        return fib(n)

            
        