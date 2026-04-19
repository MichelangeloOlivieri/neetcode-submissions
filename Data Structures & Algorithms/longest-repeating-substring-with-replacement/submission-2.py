class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return None
        
        l, r = 0, 0
        count_sub = {}
        most_frequent = -float('inf')
        max_length = -float('inf')

        while l <= r and r < len(s):
            count_sub[s[r]] = 1 + count_sub.get(s[r], 0)
            
            if count_sub[s[r]] > most_frequent:
                most_frequent = count_sub[s[r]]

            if r - l + 1 - most_frequent <= k and r - l + 1 >= max_length:
                max_length = r - l + 1
                r += 1
            else: 
                count_sub[s[l]] -= 1
                count_sub[s[r]] -= 1
                l += 1

        return max_length