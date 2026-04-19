class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # soluzione mia

        """
        1) solo interi ammessi? è garantito ci sia sempre qualche numero?
        2) Soluzione 1: scorrere prima su ogni riga/colonna, poi fare .clear di 
        elementi visti e aggiungere gli elementi che scorro all'interno della riga
        o colonna -> complessità O(n^2) per il controllo di righe o colonne; nel 
        frattempo faccio .clear di visti anche per la prima seconda e terza box
        3) Scrivo codice 
        """

        seen_row = set()
        seen_box_1 = set()
        seen_box_2 = set()
        seen_box_3 = set()
        
        seen_columns = [set() for _ in range(len(board[0]))]

        for i in range(len(board)):

            for j in range(len(board[i])):

                if board[i][j] != ".": 

                    if int(board[i][j]) in seen_row:
                        return False
                    else:
                        seen_row.add(int(board[i][j]))

                    if j in range(3):
                        if int(board[i][j]) in seen_box_1:
                            return False
                        else:
                            seen_box_1.add(int(board[i][j]))

                    if j in range(3, 6):
                        if(int(board[i][j])) in seen_box_2:
                            return False
                        else:
                            seen_box_2.add(int(board[i][j]))
                
                    if j in range(6, 9):
                        if(int(board[i][j])) in seen_box_3:
                            return False
                        else:
                            seen_box_3.add(int(board[i][j]))

                    if int(board[i][j]) in seen_columns[j]:
                        return False
                    else:
                        seen_columns[j].add(int(board[i][j]))

            seen_row.clear()

            if i == 2:
                seen_box_1.clear()
                seen_box_2.clear()
                seen_box_3.clear()
            if i == 5:
                seen_box_1.clear()
                seen_box_2.clear()
                seen_box_3.clear()
        
        return True


        """
        4) Test case: 
        - i = 0 -> board[0] = ["1", "2", ..., "."]
        - j = 0 -> board[0][0] = "1" -> seen_row = {1}, seen_box_1 = {1}, ecc, 
        seen_columns[0] = {1}
        5) Complessità temporale: O(m^2), dove m = len(board[0]) (assumo .clear()
        costante per semplicità); costo spaziale O(m^2)
        """


        