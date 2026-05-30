class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        """
        1) Empty input; example written
        2) 
        """

        if not intervals or not queries:
            return [0] * len(queries)

        def isContained(n, intv):
            return n >= intv[0] and n <= intv[1]

        res = []

        for n in queries:

            length = float('inf')

            for intv in intervals:
                if isContained(n, intv):
                    length = min(length, intv[1] - intv[0] + 1)
            
            if length == float('inf'):
                length = -1
                res.append(length)
            else:
                res.append(length)

        return res
