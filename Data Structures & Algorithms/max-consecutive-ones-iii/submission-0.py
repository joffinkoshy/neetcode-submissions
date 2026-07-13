class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr=best=0
        left=0
        n=len(nums)

        for right in range(n):
            if nums[right]==0:
                k-=1

            while k<0:
                if nums[left]==0:
                    k+=1

                left+=1

            best=max(best,right-left+1)

        return best
        