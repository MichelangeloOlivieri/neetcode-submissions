class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """
        1) Empty input; can a word be read backwards in the grid?
        2) Backtracking
        """

        # edge cases
        if not board:
            return False

        # dfs implementation
        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j, k):
            if k == len(word):
                return True
            if (i not in range(m) or 
                j not in range(n) or 
                board[i][j] == None or
                board[i][j] != word[k]):
                return False

            temp = board[i][j]
            board[i][j] = None
            for di, dj in directions:
                if dfs(i + di, j + dj, k + 1):
                    return True
            board[i][j] = temp

            return False
           
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
    
        return False

        """
        3) Syntax and dry run: ok
        4) Time complexity O(m * n * 3^(len(word))); space complexity O(len(word))
        """


            

        