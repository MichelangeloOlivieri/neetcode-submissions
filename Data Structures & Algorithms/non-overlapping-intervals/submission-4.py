class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0

        intervals.sort()

        left = intervals[0][0]
        right = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:
                left = intervals[i][0]
                right = intervals[i][1]
            elif intervals[i][1] > right:
                res += 1
            else:
                left = intervals[i][0]
                right = intervals[i][1]
                res += 1

        return res
