class MedianFinder:

    """
    1) Example?
    2) - Solution 1: use normal array as a data structure, sort it each time we add a
    value, and use usual formula for the median
    """

    def __init__(self):
        self.data = []  

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()
       
    def findMedian(self) -> float:

        if not self.data:
            return 0

        l = len(self.data)
        if l % 2:
            res = self.data[(l - 1) // 2]
            return float(res)
        else:
            res = ( self.data[(l - 1) // 2] + self.data[((l - 1) // 2) + 1] ) / 2
            return float(res)    

    """
    3) Ok
    4) Time complexity O(nlog(n!)), where n = len(self.data); space complexity O(n)
    """ 