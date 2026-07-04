class Solution:
    def minimumDifference(self, nums: List[int], k: int):
        nums.sort()
        ans = float('inf')

        for r in range(k - 1, len(nums)):
            ans = min(ans, nums[r] - nums[r - k + 1])

        return ans