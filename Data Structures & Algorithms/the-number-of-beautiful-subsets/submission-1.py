class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        res = 0
        freq = defaultdict(int)
        count = 0

        def backtrack(i):
            nonlocal res
            nonlocal count

            if i == len(nums):
                if count > 0:
                    res += 1
                return

            plus = nums[i] + k
            minus = nums[i] - k

            if freq[plus] < 1 and freq[minus] < 1:
                # choose
                freq[nums[i]] += 1
                count += 1
                backtrack(i + 1)
                # unchoose
                freq[nums[i]] -= 1
                count -= 1

            backtrack(i + 1)

        backtrack(0)
        return res

        """
        nums = [1, 3, 3], k = 2
        res = 
        backtrack(0): seen = {1} -> backtrack(2): seen = {1, 5}
        """

        
