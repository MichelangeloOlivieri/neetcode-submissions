class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        """
        limit >= max(people)
        """

        if not people:
            return 0
        
        people.sort()

        if limit < people[-1]:
            return -1

        res = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            weight = people[l] + people[r]
            if weight > limit:
                r -= 1
                res += 1
            else:
                l += 1
                r -= 1
                res += 1

        return res

        """
        Time complexity O(n * log(n)), where n = len(people); space complexity O(1)
        """