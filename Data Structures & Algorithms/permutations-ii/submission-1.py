class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        ans = []
        chosen = [False] * n

        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if chosen[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not chosen[i-1]:
                    continue

                chosen[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                chosen[i] = False

        backtrack([])
        return ans