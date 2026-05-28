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

        first = False
        second = False
        third = False

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                
                first = first or (t[0] == target[0])
                second = second or (t[1] == target[1])
                third = third or (t[2] == target[2])
                
                if first and second and third:
                    return True

        return False
            
        """
        3) Ok
        4) Time complexity O(n); space complexity O(1)
        """

        