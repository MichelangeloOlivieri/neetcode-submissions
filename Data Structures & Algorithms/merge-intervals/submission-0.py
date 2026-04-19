class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        1) Empty input; example: intervals = [[2, 3], [1, 2], [4, 5]] -> [[1, 3]]; are
        the intervals sorted in any way?
        2) - Solution 1: check every pair and merge overlapping pairs
        - Solution 2: sort the intervals based on first entry and merge overlapping
        ones
        """

        if not intervals:
            return []

        intervals.sort()
        res = []
        new = [intervals[0][0], intervals[0][1]]

        for i in range(1, len(intervals)):
            if new[1] < intervals[i][0]:
                res.append(new)
                new = [intervals[i][0], intervals[i][1]]
                continue
            else:
                new = [new[0], max(new[1], intervals[i][1])]

        res.append(new)
        return res

        """
        3) Syntax and dry run: ok
        4) Time complexity O(nlog(n)), where n = len(intervals); space complexity O(n)
        """

        