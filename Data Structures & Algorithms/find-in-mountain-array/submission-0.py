class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        """
        1) arr = [3, 10, 7, 2], target = 2 -> 3
        2) Binary Search; find the maximum first and then use binary search on both sides of the array
        """

        """
        [2, 4, 5, 2, 1], target = 2
        - l = 0, r = 5, mid = 2
        - l = 0, r = 1, mid = 0
        - l = 1, r = 1, mid = 1
        - l = 2, r = 1 -> break

        """

        l = 0
        r = mountainArr.length() - 1
        res = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            mid_value = mountainArr.get(mid)
            if mid_value == target:
                res = min(res, mid)
            if mountainArr.get(mid + 1) > mid_value:
                l = mid + 1
            else: 
                r = mid - 1

        max_index = l
        l = 0
        r = max_index

        while l <= r:
            mid = l + (r - l) // 2
            mid_value = mountainArr.get(mid)
            if mid_value == target:
                res = min(res, mid)
                break
            elif target > mid_value:
                l = mid + 1
            else:
                r = mid - 1

        l = max_index
        r = mountainArr.length() - 1

        while l <= r:
            mid = l + (r - l) // 2
            mid_value = mountainArr.get(mid)
            if mid_value == target:
                res = min(res, mid)
                break
            elif target < mid_value:
                l = mid + 1
            else:
                r = mid - 1

        return res if res != float('inf') else -1