class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)

        def backtrack(length,path,chosen):
            if length==n:
                ans.append(path[:])
                return

            for i in range(n):
                if not chosen[i]:
                    path.append(nums[i])
                    chosen[i]=True
                    backtrack(length+1,path,chosen)
                    path.pop()
                    chosen[i]=False

        chosen=[False]*n

        backtrack(0,[],chosen)
        return ans


        