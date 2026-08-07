class Solution:
    def romanToInt(self, s: str) -> int:

        """
        1) s = "I" -> 1; s = "IX" -> 9, s = "LXIV" -> 64
        2) Use a hash map to map each figure to its correspondent arab figure; when
        the last figure is bigger than the second to last perform subtraction
        """ 

        if not s:
            return 0       

        translate = {
            "I" : 1, 
            "V" : 5, 
            "X" : 10, 
            "L" : 50, 
            "C" : 100, 
            "D" : 500,
            "M" : 1000
        }

        res = 0
        last = float('inf')

        for c in s:
            n = translate[c]
            if n <= last:
                res += n
            else:
                res += n - 2 * last
            last = n

        return res

        """
        3) s = "I" -> res = 1 -> 1
            s = "IX" -> n = 1, res = 1, last = 1; n = 10, res = 1 + 10 - 2 = 9
            s = "LXIV" -> n = 50, res = 50, last = 50; 
                        n = 10, res = 60, last = 10;
                        n = 1, res = 61, last = 1;
                        n = 5, res = 64, last = 5;
            -> res = 64
            s = "CMIX" -> n = 100, res = 100, last = 100;
                        n = 1000, res = 900, last = 1000;
                        n = 1, res = 901, last = 1;
                        n = 10, res = 909, last 10;
        4) Time complexity O(len(s)); space complexity O(1)
        """