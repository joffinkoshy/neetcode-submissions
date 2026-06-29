class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        min_length=float('inf')

        l=0
        curr_sum=0

        for r in range(n):
            curr_sum+=nums[r]

            while curr_sum>=target:
                width=r-l+1
                min_length=min(min_length,width)
                curr_sum-=nums[l]
                l+=1

            
        return min_length if min_length!=float('inf') else 0

        