class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        n=len(candidates)
        

        def backtrack(start,remaining,path):
            if remaining==0:
                ans.append(path[:])
                return

            for i in range(start,n):
                if i>start and candidates[i]==candidates[i-1]:
                    continue

                if candidates[i]>remaining:
                    break

                path.append(candidates[i])
                backtrack(i+1,remaining-candidates[i],path)
                path.pop()

        backtrack(0,target,[])
        return ans            

        