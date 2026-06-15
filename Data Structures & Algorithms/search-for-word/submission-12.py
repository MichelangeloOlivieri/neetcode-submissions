from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        # 1. SOTA Pruning: Controllo di Frequenza Pre-DFS
        # Se la scacchiera non ha nemmeno le lettere sufficienti, interrompiamo in O(M*N)
        board_freq = sum(map(Counter, board), Counter())
        word_freq = Counter(word)
        for char, count in word_freq.items():
            if board_freq[char] < count:
                return False
                
        # 2. SOTA Pruning: Pathological Case Reversal
        # Se il primo carattere della parola è più comune dell'ultimo,
        # invertiamo la parola. Il DFS partirà dal carattere più RARO,
        # causando un "branch pruning" quasi immediato.
        if board_freq[word[0]] > board_freq[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True
                
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False
                
            # 3. SOTA Memory: In-Place Visited Marker
            # Invece di un Set() costoso, distruggiamo temporaneamente la cella
            temp = board[r][c]
            board[r][c] = '#'
            
            # DFS sulle 4 direzioni
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
                   
            # Backtracking: Ripristiniamo la cella originale
            board[r][c] = temp
            
            return res

        # 4. Innesco del Backtracking
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                        
        return False