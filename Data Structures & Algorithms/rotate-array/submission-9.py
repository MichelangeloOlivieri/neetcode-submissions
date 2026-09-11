class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n

        if k == 0 or n <= 1:
            return

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        m = gcd(n, k)
        for i in range(m):
            curr = i
            curr_val = nums[i]
            
            while True:
                next_idx = (curr + k) % n
                nums[next_idx], curr_val = curr_val, nums[next_idx]
                curr = next_idx

                if curr == i:
                    break

        """
        - Time complexity O(N), where N = len(nums)
        - Space complexity O(1)
        """