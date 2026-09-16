class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a
            
        total_len = len(a) + len(b)
        half_len = total_len // 2
        left, right = 0, len(a) - 1
        
        while True:
            i = (left + right) // 2
            j = half_len - i - 2
            
            a_left = a[i] if i >= 0 else float("-inf")
            a_right = a[i + 1] if (i + 1) < len(a) else float("inf")
            b_left = b[j] if j >= 0 else float("-inf")
            b_right = b[j + 1] if (j + 1) < len(b) else float("inf")
            
            if a_left <= b_right and b_left <= a_right:
                if total_len % 2 != 0:
                    return float(min(a_right, b_right))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
            
            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1

        """
        - Time complexity O(log(min(m, n))), where m = len(nums1) and n = len(nums2)
        - Space complexity O(1)
        """