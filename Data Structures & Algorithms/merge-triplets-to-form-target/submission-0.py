class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        """
        1) Empty input; example written
        2) Order does not count, only counts which triplets you choose; so go through 
        the list and discard whatever cur goes beyond one of the three thresholds
        given by the target
        """

        if not triplets and not target:
            return True
        if not triplets:
            return False
        if not target:
            return True

        def merge(a, b):
            return [max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2])]

        def check(a, b):
            return a[0] <= b[0] and a[1] <= b[1] and a[2] <= b[2]

        cur = [-float('inf'), -float('inf'), -float('inf')]

        for i in range(len(triplets)):
            if check(triplets[i], target):
                cur = merge(cur, triplets[i])
                if cur == target:
                    return True

        return False
            
        """
        3) Ok
        4) Time complexity O(n); space complexity O(1)
        """

        