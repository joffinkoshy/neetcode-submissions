class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest=curr=1
        prev=nums[0]

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                curr+=1
            else:
                curr=1

            longest=max(longest,curr)

        return longest


        