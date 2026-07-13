class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product=1
        left=0
        n=len(nums)
        ans=0
        if k <= 1:

            return 0

        for right in range(n):
            product*=nums[right]

            while product>=k:
                product//=nums[left]
                left+=1

            ans+=right-left+1

        return ans

        