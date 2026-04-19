class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        """
        1) Empty input; is result guaranteed in 32-bit? I guess so; can numbers be 
        negative?
        2) Use operators like &, |
        """

        if not a and not b:
            return 0
        if not a:
            return b
        if not b:
            return a

        mask = 0xFFFFFFFF # 1. Definisci il limite a 32-bit

        # Se b entra come negativo (bit infiniti), lo mascheriamo subito per sicurezza
        b = b & mask 

        while b != 0:
            temp = a
            a = (a ^ b) & mask             # 2. Taglia a 32-bit
            b = ((temp & b) << 1) & mask   # 3. Taglia a 32-bit

        # 4. Restituisci 'a' se positivo. 
        # Se è negativo (maggiore di 0x7FFFFFFF), "riaccendi" gli 1 infiniti a sinistra 
        # con ~(a ^ mask) per far capire a Python che è un numero negativo.
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)

        """
        3) Ok
        4) Time complexity O(1); space complexity O(1)
        """


