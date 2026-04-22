class Solution:           

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length

        return res

        # soluzione mia

        """
        1) Quali caratteri sono ammessi? Ammessa stringa vuota?
        2) Soluzione 1: encode crea una stringa dove prima di ogni elemento della 
        lista viene messo il numero di caratteri dell'elemento; in questo modo
        decode legge il primo numero, taglia la stringa e passa alla prossima; non
        ho altre soluzioni in mente   
        3) Scrivo codice
        4) strs = ["Hello", "World"]
        numbered_list = ["5", "Hello", "5", "World"]
        numbered_string = 5Hello5World
        s_next = "Hello", s = "5World" -> original_list = ["Hello", ...]
        5) Complessità temporale per encode: O(mn) dove m = len(strs), n = 
        = max(len(s) for s in strs); complessità temporale per decode: O(mn); 
        complessità spaziale per encode: O(mn); complessità spaziale per 
        decode: O(mn)
        """