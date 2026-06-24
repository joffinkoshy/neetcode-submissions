class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        chosen=[False]*n

        def backtrack(path,length):
            if length==n:
                ans.append(path[:])
                return
            
            
            for i in range(n):
                if chosen[i]:
                    continue
                    
                if i>0 and chosen[i-1] and nums[i]==nums[i-1]:
                    continue

                path.append(nums[i])
                chosen[i]=True

                backtrack(path,length+1)

                path.pop()
                chosen[i]=False
            
            
                


        backtrack([],0)
        return ans
        