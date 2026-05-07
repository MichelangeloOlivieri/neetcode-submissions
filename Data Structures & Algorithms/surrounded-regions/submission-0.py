class Solution:
    def solve(self, board: List[List[str]]) -> None:

        """
        1) Empty input; example seen; squares on edge never considered surrounded
        2) First bfs starting at the edge squares where you have 'O', then double for
        cycle
        """

        if not board: 
            return

        m = len(board)
        n = len(board[0])
        visited = set()
        q = collections.deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(i, j):
            board[i][j] = 'Y'
            visited.add((i, j))
            q.append((i, j))

            while q:

                row, col = q.popleft()                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (new_row in range(m)
                    and new_col in range(n)
                    and (new_row, new_col) not in visited
                    and board[new_row][new_col] == 'O'):
                        board[new_row][new_col] = 'Y'
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))

        for i in range(m):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][n - 1] == 'O':
                bfs(i, n - 1)     

        for j in range(n):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[m - 1][j] == 'O':
                bfs(m - 1, j)  

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O' 

        """
        3) Ok
        4) Time complexity O(m * n); space complexity O(m * n)
        """