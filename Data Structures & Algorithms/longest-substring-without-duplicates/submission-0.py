class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        1) Quindi per esempio "abdcdce" -> "abdc", corretto? Quali caratteri stiamo accettando? "cdcadscd"; immagino che a parità di lunghezza sia ininfluente
        2) - Metodo 1: effettuare un doppio scorrimento della stringa fissando un indice e scorrendo con un altro in avanti; fermarsi quando si trova un 
        carattere che si è già incontrato (salvato per esempio in un Set), e salvare tutte le sottostringhe in un dizionario con annessa lunghezza; infine 
        prendere il massimo
        - Metodo 2: 
        3) Scrivo codice
        """

        res = 0
        # Non serve il dizionario enorme, basta tenere il massimo numero
        max_len = 0 

        for i in range(len(s)):
            seen = set() # NUOVO set per ogni sottostringa che parte da 'i'
            
            for j in range(i, len(s)):
                if s[j] in seen:
                    # Duplicato trovato! La sottostringa valida finisce qui.
                    # Lunghezza attuale = j - i
                    max_len = max(max_len, j - i)
                    break 
                else:
                    seen.add(s[j])
                    # Se siamo arrivati all'ultimo carattere senza break
                    # dobbiamo contare anche questo caso!
                    if j == len(s) - 1:
                        max_len = max(max_len, j - i + 1)
        
        return max_len


        """
        4) Test case: - "cacda"
        - i = 0; j = 0; s[j] = c; characters = {c}; 
                j = 1; s[j] = a; characters = {c, a};
                j = 2; s[j] = c; current = "ca"; candidates[2] = ["ca"]; characters = {}
        - i = 1; j = 1; s[j] = a; characters = {a};
                j = 2; s[j] = c; characters = {a, c};
                j = 3; s[j] = d; characters = {a, c, d};
                j = 4; s[j] = a; current = "acd"; candidates[3] = ["acs"]; characters = {}
        """

        """
        DI SEGUITO L'ORRORE CHE IN REALTA' AVEVO SCRITTO 

        import random

        res = 0
        characters = set()
        candidates = defaultdict(list)

        for i in range(len(s)):
            for j in range(i, len(s)):

                if s[j] in characters:
                    current = s[i : j]
                    candidates[len(current)].append(current)
                    characters.clear()
                    break
                else:
                    characters.add(s[j])
                    if j == len(s) - 1:
                        characters.clear()
                        return len(s[i : j + 1])
        
        chosen_list = candidates[max(candidates)]
        string = random.choice(chosen_list)

        return len(string)
        """


