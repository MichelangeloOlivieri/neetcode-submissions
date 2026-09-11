class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        1) nums = [3, 2, 1, 4], k = 2
        - prev = 0, curr = 2, prev_val = 1, curr_val = 3, nums[2] = 1, prev_val = 3
        - prev = 2, curr = 0: break, nums[0] = 3
        -
        2) Two Pointers
        """

        if not nums or k == 0:
            return None

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        k = k % len(nums)

        def aux(i):
            prev = i % len(nums)
            curr = (i + k) % len(nums)
            prev_val = nums[prev]
            while curr != i:
                curr_val = nums[curr]
                nums[curr] = prev_val
                prev_val = curr_val
                prev = curr % len(nums)
                curr = (curr + k) % len(nums)
            nums[curr] = prev_val

        m = gcd(len(nums), k)
        for i in range(m):
            aux(i)

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """  