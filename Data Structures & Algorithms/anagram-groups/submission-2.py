class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # soluzione mia

        """
        1) Caratteri solo alfabetici latini is.alpha()? Devo gestire input vuoto?
        Devo gestire upper/lowercase? Dagli esempi vedo solo lowercase, quindi 
        assumo tutto lowercase
        2) Soluzione 1: fare una hash map dove le chiavi sono le stringhe ordinate
        e i valori array di stringhe che sono anagrammi; per farlo, scorrere 
        l'array di stringhe, vedere se la classe di equivalenza c'è già o meno; 
        in totale dovrebbe venire spazio O(len(strs)) e tempo O(max(len(s))); 
        sembra già ottimizzata, quindi procedo
        3) Scrivo il codice
        """

        Visited = {}
        Output = []

        for string in strs:
            ordered_list = sorted(string)
            ordered_string = "".join(ordered_list)
            if ordered_string in Visited:
                Visited[ordered_string].append(string)
            else: 
                Visited[ordered_string] = [string]

        for ordered_string in Visited:
            Output.append(Visited[ordered_string])

        return Output

        """
        4) Test case:
        - strs = ["act", "pots", "tops", "cat", "stop", "hat"]
        - string = "act"; ordered_string = "act"; Visited = {["act"]}
        - string = "pots"; ordered_string = "opst"; Visited = {["act"]:["act"], 
        ["opst"]:["opst"]}
        - string "tops"; ordered_string = "opst"; Visited = {["act"]:["act"], 
        ["opst"]:["pots", "tops"]}
        - ecc
        - Output = {["act"], ["pots", "tops", ...], ...}
        5) complessità temporale: O(len(strs)) * O(max(len(string) for string 
        in strs)); complessità spaziale: O(len(strs))
        """





        