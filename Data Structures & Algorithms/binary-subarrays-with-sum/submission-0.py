class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atMost(nums,k):
            if k<0:
                return 0

            left=0
            curr=0
            ans=0

            for right in range(len(nums)):
                curr+=nums[right]

                while curr>k:
                    curr-=nums[left]
                    left+=1

                ans+=right-left+1 # counting all valid subarrays endig at right
            return ans

        return atMost(nums,goal)-atMost(nums,goal-1)


        
        