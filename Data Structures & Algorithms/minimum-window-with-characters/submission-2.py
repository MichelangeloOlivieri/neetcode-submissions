class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # soluzione ottimizzata

        if len(s) < len(t) or t == "":
            return ""

        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        window = {}
        have = 0
        need = len(count_t)
        res_id = [-1, -1]
        res_length = float('inf')
        l = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < res_length:
                    res_length = r - l + 1
                    res_id = [l, r]

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l = res_id[0]
        r = res_id[1]

        return s[l: r + 1] if res_length != float('inf') else ""




        
        