class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        1) nums1 = [1, 3, 4, 6, 0, 0], nums2 = [2, 5] -> nums1 = [1, 2, 3]
        2) merge step of the MergeSort algorithm
        [, 2, 3, 4, 5, 6]
        """ 

        last = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last -= 1
                i -= 1
            else:
                nums1[last] = nums2[j]
                last -= 1
                j -= 1

        while i >= 0:
            nums1[last] = nums1[i]
            last -= 1
            i -= 1
        while j >= 0:
            nums1[last] = nums2[j]
            last -= 1
            j -= 1