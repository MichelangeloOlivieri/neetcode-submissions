class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort()
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= curr_end:
                curr_start = start
                curr_end = end
            else:
                if end >= curr_end:
                    res += 1
                else:
                    curr_start = start
                    curr_end = end
                    res += 1

        return res