class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        """
        1) devo gestire il caso stringa vuota? i caratteri sono quelli latini e non
        ci sono numeri?
        2) soluzione 1: confrontare le lunghezze, se diverse restituisco subito 
        false (tempo O(n) per len()); se no, creare due dizionari coi caratteri
        delle stringhe e relative frequenze (spazio O(n)); confrontare i dizionari,
        se sono uguali, allora True 
        3) scrivo codice
        """

        if len(s) != len(t):
            return False

        else:
            dictionary_s = {}
            for c in s:
                dictionary_s[c] = dictionary_s.get(c, 0) + 1

            dictionary_t = {}
            for c in t:
                dictionary_t[c] = dictionary_t.get(c, 0) + 1

            if dictionary_s == dictionary_t:
                return True
            else:
                return False

            """
            4) test case: s = "racecar", t = "carrace"
            len(s) = 7 = len(t)
            dictionary_s = {r:2, a:2, c:1, e:1}; dictionary_t = {c:2, a:2, r:2, e:1}
            5) complessità temporale O(n), spaziale O(n)
            """