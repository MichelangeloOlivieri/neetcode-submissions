class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # mio tentativo

        """
        1) Per vedere se ho capito: s = "asbabb", t = "aab" -> res = "asba"; quali caratteri
        assumiamo che siano presenti?
        2) - Soluzione 1: fare una hash map {[lettera: count]} per le lettere di t, fare un
        ciclo sulle lettere di s e rimuoverle se stanno nella hash map aggiornando il contatore
        delle lettere di t; quando il contatore è azzerato -> NO
        """

        if len(s) < len(t):
            return ""

        target_counts = Counter(t) # Dizionario con le frequenze di t
        min_len = float('inf')
        best_str = ""

        # Doppio ciclo per testare TUTTE le sottostringhe possibili
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                
                # Contiamo i caratteri della sottostringa attuale
                sub_counts = Counter(substring)
                
                # Verifichiamo se contiene tutti i caratteri di t nelle giuste quantità
                is_valid = True
                for char, count in target_counts.items():
                    if sub_counts[char] < count:
                        is_valid = False
                        break
                
                # Se è valida e più corta del nostro record, aggiorniamo!
                if is_valid and len(substring) < min_len:
                    min_len = len(substring)
                    best_str = substring

        return best_str