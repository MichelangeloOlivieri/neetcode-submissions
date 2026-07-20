class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        1) nums1 = [1, 3, 4, 5, 0, 0], nums2 = [2, 6] -> nums1 = [1, 2, 3]
        2) merge step of the MergeSort algorithm
        [1, 2, 4, 5, 0, 0]
        """       

        stack = []
        i = 0
        j = 0
        while i <= m - 1 and j <= n - 1:
            if nums1[i] <= nums2[j]:
                stack.append(nums1[i])
                i += 1
            else:
                stack.append(nums2[j])
                j += 1
        
        if i <= m - 1:
            while i <= m - 1:
                stack.append(nums1[i])
                i += 1
        elif j <= n - 1:
            while j <= n - 1:
                stack.append(nums2[j])
                j += 1 

        for k in range(len(stack)):
            nums1[k] = stack[k]