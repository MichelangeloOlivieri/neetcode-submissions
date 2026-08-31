class Solution:
    def decodeString(self, s: str) -> str:

        """
        1) "2[aa]1[]10[b]" -> "aaaabbbbbbbbbb"
        2) String, Two Pointers
        """

        if not s:
            return ""

        digits = {
            "0" : 0, 
            "1" : 1, 
            "2" : 2, 
            "3" : 3, 
            "4" : 4, 
            "5" : 5, 
            "6" : 6, 
            "7" : 7, 
            "8" : 8, 
            "9" : 9
        }
        res = []

        i = 0
        while i < len(s):

            if s[i] not in digits and s[i] != "[":
                res.append(s[i])
            
            # if you find an integer
            arr = []
            while i < len(s) and s[i] in digits:
                arr.append(digits[s[i]])
                i += 1

            n = 0
            j = 0
            while arr:
                n += (10 ** j) * arr.pop()
                j += 1
            
            # if you find a "["
            if s[i] == "[":

                count_left = 1
                count_right = 0
                t = ""

                i += 1
                while i < len(s):
                    if s[i] == "[":
                        count_left += 1
                    elif s[i] == "]":
                        count_right += 1
                        if count_right == count_left:
                            break
                    t += s[i]
                    i += 1

                # t = "b"
                tba = self.decodeString(t)
                while n > 0:
                    res.append(tba)
                    n -= 1

            i += 1

        return "".join(res)

        """
        s = "2[a3[b]]c", res = []
        - i = 0: s[i] = "2", arr = [2]
        - i = 1: 
            -> s[i] = "[", n = 2
            -> count_left = 2, count_right = 1, t = ""
            -> i = 2: t = "a"
            -> i = 3: t = "a3"
            -> i = 4: t = "a3[b]"
            -> tba = "abbb"
            -> res = "abbbabbb"
        """

        """
        s = "a3[b]", res = []
        - i = 0: s[0] = "a", res["a"]
        - i = 1: s[1] = "3", n = 3
        - i = 2:
            -> s[i] = "["
            -> t = "b"
        """



        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(n)
        """