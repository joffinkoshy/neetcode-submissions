class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])

        pacific=set()
        atlantic=set()

        def dfs(r,c,visited):
            visited.add((r,c))

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)


         # Pacific

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)

        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)

        ans = []

        for i in range(m):

            for j in range(n):

                if (i, j) in pacific and (i, j) in atlantic:

                    ans.append([i, j])

        return ans
        