class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        best=1
        n=len(nums)

        window_sum=0
        left=0

        for right in range(len(nums)):
            window_sum+=nums[right]

            while nums[right]*(right-left+1)-window_sum>k:
                window_sum-=nums[left]
                left+=1

            best=max(best,right-left+1)

        return best
    

                
        