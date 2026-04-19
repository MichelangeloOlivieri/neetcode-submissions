class Solution:           

    def encode(self, strs: List[str]) -> str:

        numbered_list = []
        for stringa in strs:
            numbered_list.append(str(len(stringa)))
            numbered_list.append("#")
            numbered_list.append(stringa)
        
        numbered_string = "".join(numbered_list)

        return numbered_string

    def decode(self, s: str) -> List[str]:

        original_list = []
        i = 0
    
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length
            original_list.append(s[word_start : word_end])
            i = word_end

        return original_list

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
        5) Complessità temporale per encode: O(len(strs))*O(time(len_function)); 
        complessità temporale per decode: O(len(strs)) + O(max(len(s) for s in strs));
        complessità spaziale per encode: O(len(strs)); complessità spaziale per 
        decode: O(len(strs))
        """