from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])
        q = deque()

        # Add all boundary O's
        for i in range(m):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][n - 1] == "O":
                q.append((i, n - 1))

        for j in range(n):
            if board[0][j] == "O":
                q.append((0, j))
            if board[m - 1][j] == "O":
                q.append((m - 1, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()

            


            board[x][y] = "#"

            for dx, dy in directions:
                r,c=x + dx, y + dy
                if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                    q.append((r,c))

        # Restore safe cells and flip surrounded ones
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"