from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])

        INF=2**31-1

        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))


        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            i,j=q.popleft()

            for di,dj in directions:
                ni,nj=i+di,j+dj

                if (
                    0<=ni<m and
                    0<=nj<n and
                    grid[ni][nj]==INF
                ):
                    grid[ni][nj]=grid[i][j]+1
                    q.append((ni,nj))

        
        