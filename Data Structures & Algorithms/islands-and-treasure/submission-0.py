class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])

        INF=2**31-1

        def dfs(i,j,dist):

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == -1:
                return

            if dist > grid[i][j]:
                return


            grid[i][j] = dist

            dfs(i+1,j,dist+1)
            dfs(i,j+1,dist+1)
            dfs(i-1,j,dist+1)
            dfs(i,j-1,dist+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    dfs(i,j,0)

        