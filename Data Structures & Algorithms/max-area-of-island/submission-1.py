class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0

        def dfs(i,j):

            if not (0<=i<m and 0<=j<n and grid[i][j]==1):
                return 0

            grid[i][j]=0

            left=dfs(i,j-1)
            right=dfs(i,j+1)
            up=dfs(i-1,j)
            down=dfs(i+1,j)

            return 1+left+right+up+down

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans=max(ans,dfs(i,j))

        return ans

            
        