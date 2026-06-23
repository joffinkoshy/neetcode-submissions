class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]

        def backtrack(i,path,length):
            if length==k:
                ans.append(path[:])
                return

            if i>n:
                return
            

            path.append(i)
            backtrack(i+1,path,length+1)
            path.pop()
            backtrack(i+1,path,length)

        backtrack(1,[],0)
        return ans
        