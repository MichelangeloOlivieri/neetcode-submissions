"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        """
        1) Empty input; is the input sorted?
        2) - Solution 1: sort th input based on self.start
        """

        if not intervals:
            return True

        intervals.sort(key = lambda i : i.start)
        for i in range(len(intervals) - 1):
            if intervals[i + 1].start < intervals[i].end:
                return False

        return True

        """
        3) Syntax and dry run: ok
        4) Time complexity O(nlog(n)) where n = len(intervals); space complexity O(1)
        """


        
