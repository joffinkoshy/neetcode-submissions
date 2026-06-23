class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[0]
        
        def backtrack(i,curr_xor):
            if i==n:
                ans[0]+=curr_xor
                return

            backtrack(i+1,curr_xor^nums[i])
            backtrack(i+1,curr_xor)

        backtrack(0,0)
        return ans[0]
        
       
                
        