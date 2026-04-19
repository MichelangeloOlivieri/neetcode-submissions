class Solution:
    def numDecodings(self, s: str) -> int:

        """
        1) Empty input
        2) Dynamic programming solution
        """

        # base cases
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        
        dp = [0] * len(s)
        dp[0] = 1

        for i in range(1, len(s)):

            # next one is zero
            if s[i] == '0': 
                # Uno '0' DEVE per forza accoppiarsi col precedente ('10' o '20').
                if s[i - 1] == '1' or s[i - 1] == '2':
                    # I modi totali sono esattamente quelli che avevamo due passi fa.
                    # Se siamo all'indice 1, non esiste un i-2, quindi il valore è 1.
                    dp[i] = dp[i - 2] if i >= 2 else 1
                else: 
                    # Uno zero non preceduto da 1 o 2 (es. '30' o '00') blocca tutto.
                    return 0

            # next one is not zero
            if s[i] != '0': 
                # Dato che non è zero, può sempre stare da solo. 
                # Eredita tutti i percorsi del passo precedente.
                dp[i] = dp[i - 1]
                
                # Se forma anche una coppia valida col precedente ("11" a "26"), 
                # AGGIUNGIAMO a dp[i] anche i percorsi di due passi fa.
                if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                    dp[i] += dp[i - 2] if i >= 2 else 1

        return dp[len(s) - 1]

        """
        3) Syntax and dry run: seems ok
        4) Time complexity O(n); space complexity O(n)
        """



        
        