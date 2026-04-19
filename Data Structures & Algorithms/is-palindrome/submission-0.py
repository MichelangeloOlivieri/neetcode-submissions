class Solution:
    def isPalindrome(self, s: str) -> bool:

        # soluzione mia

        """
        1) La questione delle maiuscole e dei caratteri possibili è già stata 
        trattata, quindi ok
        2) Soluzione 1: prendo la stringa, la scorro per eliminare tutti i
        caratteri non is.alnum(); scorro di nuovo la stringa per invertirla in
        tempo O(n) facendo le sostituzioni; confronto la stringa iniziale con 
        quella invertita; tutto avviene in tempo O(n), quindi sembra efficiente
        3) Scrivo codice
        """

        clean_s = "".join(c.lower() for c in s if c.isalnum() == True)

        return clean_s == clean_s[::-1]

        """
        4) Test case: - s = "tab a cat"
        - s = "tabacat"
        - s_inverse = "tacabat"
        5) Complessità temporale O(len(s)); complessità spaziale O(1)
        """
        
                


        