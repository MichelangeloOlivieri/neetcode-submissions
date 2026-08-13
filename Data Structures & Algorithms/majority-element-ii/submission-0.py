class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        """
        1) nums = [1, 2, 1] -> [1]
        2) Brute Force, Array problem
        """

        if not nums:
            return []

        res = []
        threshold = len(nums) // 3
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1 
        for n in freq:
            if freq[n] > threshold:
                res.append(n)

        return res

        """
        3) nums = [1], threshold = 0, freq = {1 : 1} -> [1]
        4) Time complexity O(n), where n = len(nums); space complexity O(n)
        """