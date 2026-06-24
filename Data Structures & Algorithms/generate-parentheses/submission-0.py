class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opening=n
        closing=n
        ans=[]

        def backtrack(opening,closing,path):
            if closing>opening:
                return

            if opening+closing==2*n:
                ans.append(''.join(path[:]))
                return

            if opening<n:
                path.append('(')
                backtrack(opening+1,closing,path)
                path.pop()

            
            if closing<opening:
                path.append(')')
                backtrack(opening,closing+1,path)
                path.pop()

        backtrack(0,0,[])
        return ans


        