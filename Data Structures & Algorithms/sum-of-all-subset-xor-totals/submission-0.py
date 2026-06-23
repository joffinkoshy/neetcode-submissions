class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[]
        result=0
        def XOR(arr):
            res=0

            for num in arr:
                res=res^num

            return res

        def backtrack(i,path):
            if i==n:
                ans.append(path[:])
                return

            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
            backtrack(i+1,path)

        backtrack(0,[])
        
        for arr in ans:
            result+=XOR(arr)

        return result

                
        