class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        min_difference=float('inf')

        l=0

        for r in range(k-1,n):
            min_difference=min(min_difference,nums[r]-nums[l])
            l+=1

        return min_difference





        