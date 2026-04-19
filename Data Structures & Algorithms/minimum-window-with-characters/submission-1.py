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

        t_count = defaultdict(int)
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        min_length = float('inf')
        best_string = ""

        for i in range(len(s)):
            for j in range(i, len(s)):

                substr = s[i: j + 1]
                substr_count = defaultdict(int)
                for c in substr:
                    substr_count[c] = 1 + substr_count.get(c, 0)

                valid = 1
                for c in t:
                    if substr_count[c] < t_count[c]:
                        valid = 0
                        break

                if valid and len(substr) < min_length:
                    min_length = len(substr)
                    best_string = substr

        return best_string
