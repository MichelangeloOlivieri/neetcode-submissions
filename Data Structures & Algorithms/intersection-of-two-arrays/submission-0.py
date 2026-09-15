class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1:
            return []
        if not nums2:
            return []

        first = set(nums1)
        second = set(nums2)
        res = []

        for n in first:
            if n in second:
                res.append(n)

        return res

        """
        - Time complexity O(max(m, n)), where m = len(nums1) and n = len(nums2)
        - Space complexity O(max(m, n))
        """