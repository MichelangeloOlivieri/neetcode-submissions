class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # Minimo di parentesi '(' aperte
        cmax = 0  # Massimo di parentesi '(' aperte

        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:
                cmin -= 1  # Simulo che sia ')'
                cmax += 1  # Simulo che sia '('

            # Controllo 1: Se il massimo scende sotto zero, 
            # significa che ci sono inesorabilmente troppe ')'
            if cmax < 0:
                return False

            # Controllo 2: Il minimo non può mai essere negativo.
            # Se lo è, significa che un '*' che abbiamo contato come ')' 
            # deve in realtà essere ignorato (contato come spazio vuoto).
            if cmin < 0:
                cmin = 0

        # Alla fine della stringa, se c'è la possibilità matematica
        # che non ci siano parentesi aperte rimaste, è valida.
        return cmin == 0