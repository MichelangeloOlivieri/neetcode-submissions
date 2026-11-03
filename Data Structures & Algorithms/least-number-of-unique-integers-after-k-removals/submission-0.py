class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        if not arr:
            return 0

        freq = defaultdict(int)
        for n in arr:
            freq[n] += 1

        frequencies = []
        for n in freq:
            c = freq[n]
            frequencies.append([c, n])

        frequencies.sort()

        for c, n in frequencies:
            if k >= c:
                k -= c
                del freq[n]
            else:
                break

        return len(freq)

        """
        - Time complexity O(n * log(n)), where n = len(arr)
        - Space complexity O(n)
        """       