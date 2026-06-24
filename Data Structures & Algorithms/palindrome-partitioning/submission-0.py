class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        ans=[]


        for i in range(n-1,-1,-1):
            for j in range(i,n):
                
                if s[i]==s[j]:
                    if j-i<=2:
                        dp[i][j]=True

                    else:
                        dp[i][j]=dp[i+1][j-1]


        def backtrack(start,path):
            if start==n:
                ans.append(path[:])
                return

            for end in range(start,n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end+1,path)
                    path.pop()

        backtrack(0,[])
        return ans
                




        


        