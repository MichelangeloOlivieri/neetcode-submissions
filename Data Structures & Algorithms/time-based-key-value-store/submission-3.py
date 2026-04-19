class TimeMap:

    """
    1) Is it possible to have two separate events at the same timestamp? What should one return
    in such case?
    2) Straightforward system design solution
    """

    def __init__(self):
        self.events = defaultdict(list)

        """
        self.events = {"key" : []}
        """
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.events[key].append([value, timestamp]) 

        """
        self.events = {key : [[value, timestamp]]}
        """

    def get(self, key: str, timestamp: int) -> str:

        l = 0
        r = len(self.events[key]) - 1

        if not self.events[key]:
            return ""

        while l <= r:

            mid = (l + r ) // 2
            event = self.events[key][mid]

            if event[1] == timestamp:
                return event[0]
            elif event[1] < timestamp:
                l = mid + 1
            elif event[1] > timestamp:
                r = mid - 1

        if r >= 0:
            return self.events[key][r][0]
        else:
            return ""

    """
    3) Dry run: I think it is ok (troppo scomodo da provare)
    4) Time complexity O(log(n)); space complexity O(n * m), where m is the length of the longest
    string
    """

        
