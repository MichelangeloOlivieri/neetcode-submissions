class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals and not newInterval:
            return []
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        res = []

        for i in range(len(intervals)):
            new_start, new_end = newInterval
            start, end = intervals[i]
            
            if new_end < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < new_start:
                res.append(intervals[i])
            else: 
                newInterval = [min(new_start, start), max(new_end, end)]

        res.append(newInterval)
        return res

"""
- Time complexity: O(n * log(n)), where n = len(intervals).
- Space complexity: O(n).
"""