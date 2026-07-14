class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        if not trips:
            return True

        pass_change = [0] * 1001

        for t in trips:
            pass_change[t[1]] += t[0]
            pass_change[t[2]] -= t[0]

        curr_pass = 0
        for change in pass_change:
            curr_pass += change
            if curr_pass > capacity:
                return False
            
        return True