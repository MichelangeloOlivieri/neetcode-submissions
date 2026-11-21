class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        last = m + n - 1
        i = m - 1
        j = n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1

            last -= 1

"""
- Time complexity: O(m + n).
- Space complexity: O(1).
"""