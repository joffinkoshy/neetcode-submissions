from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        q=deque()
        fresh=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1
        ans=0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        ans=0

        while q:
            i,j,time=q.popleft()
            ans=time
            
            for di,dj in directions:
                r,c=i+di,j+dj

                if 0<=r<m and 0<=c<n and grid[r][c]==1:
                    grid[r][c]=2
                    fresh-=1
                    q.append((r,c,time+1))

        if fresh==0:
            return ans
        else:
            return -1


        