class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        
        intervals.sort(key=lambda x : x[1])
        current = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < current:
                res += 1
            else:
                current = end

        return res
        