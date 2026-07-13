class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(grumpy)

        l=0
        k=minutes
        extra=best=0
        base=0
        for i in range(n):
            if grumpy[i]==0:
                base+=customers[i]

        

        for r in range(n):
            if grumpy[r]==1:
                extra+=customers[r]

            while r-l+1>minutes:
                if grumpy[l]==1:
                    extra-=customers[l]

                l+=1

            best=max(best,extra)

        return base+best



        