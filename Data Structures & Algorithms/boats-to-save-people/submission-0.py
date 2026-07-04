class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        """
        limit >= max(people)
        """

        if not people:
            return 0

        if limit < max(people):
            return -1
        
        n = len(people)
        if limit >= sum(people):
            return ((n - 1) // 2) + 1
        
        people.sort()
        res = 0
        l = 0
        r = n - 1

        while l <= r:
            if l != r:
                weight = people[l] + people[r]
                if weight > limit:
                    r -= 1
                    res += 1
                else:
                    l += 1
                    r -= 1
                    res += 1
            else:
                l += 1
                r -= 1
                res += 1

        return res

        """
        Time complexity O(n * log(n)); space complexity O(1)
        """