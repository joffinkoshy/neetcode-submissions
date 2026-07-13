from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(nums,k):
            if k<0:
                return 0

            left=0
            count=defaultdict(int)
            distinct=0
            ans=0

            for right in range(len(nums)):
                if count[nums[right]]==0:
                    distinct+=1

                count[nums[right]]+=1

                while distinct>k:
                    count[nums[left]]-=1
                    if count[nums[left]]==0:
                        distinct-=1

                    left+=1

                ans+=right-left+1

            return ans

        return atMost(nums,k)-atMost(nums,k-1)

        