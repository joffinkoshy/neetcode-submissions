class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            comp=set()
            for j in range(i + 1, len(nums)):
                if target-nums[j] in comp:
                    ans.append([nums[i],nums[j],target-nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1

                comp.add(nums[j])

        res = []
        for tri in ans:
            if tri not in res:
                res.append(tri)
        return res