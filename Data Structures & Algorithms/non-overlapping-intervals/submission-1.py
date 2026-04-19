class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        """
        1) Empty input; example: intervals = [[1, 3], [3, 5], [2, 4]] -> 1
        2) - Solution 1: sort the intervals 
        """

        if not intervals:
            return 0

        intervals.sort(key = lambda i: i[0])
        res = 0   
        curr = [intervals[0][0], intervals[0][1]]     
        
        for i in range(1, len(intervals)):
            if curr[1] <= intervals[i][0]:
                curr = [intervals[i][0], intervals[i][1]]
            else: 
                if curr[1] >= intervals[i][1]:
                    curr[0] = intervals[i][0]
                    curr[1] = intervals[i][1]
                    res += 1
                else:
                    res += 1

        return res

        """
        3) Syntax and dry run:
        4) Time complexity O(nlog(n)), where n = len(intervals); space complexity O(1)
        """

        