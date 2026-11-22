class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if not arr:
            return []

        n = len(arr)

        if k >= n:
            return arr

        # idea: binary search on the left boundary of the window, not on the value itself
        
        l = 0
        r = n - k - 1

        while l <= r:
            mid = l + (r - l) // 2
            # if the distance is greater to the left, go right
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid - 1

        return arr[l : l + k]

"""
- Time complexity: O(log(n - k) + k), where n = len(arr).
- Space complexity: O(k) for the output result.
"""