class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        """
        1) What is the median actually? Can you give me a mathematical definition?
        2) - Solution 1: a brute force solution would be to link the two lists, sort the new list
        and then use the definition of mean to compute it; this would run in O((m + n)log(m + n))
        """

        import statistics

        nums = nums1 + nums2
        nums.sort()

        return statistics.median(nums)

        """
        3) No need to check anything as this is trivially ok
        4) Already done above
        """

        