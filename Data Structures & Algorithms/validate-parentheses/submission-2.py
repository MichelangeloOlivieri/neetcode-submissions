class Solution:
    def isValid(self, s: str) -> bool:

        # tentativo mio

        """
        1) Niente da dire
        2) Dopo aver letto il suggerimento, implemento la soluzione inefficiente
        """

        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        return len(s) == 0

        """
        3) 
        """