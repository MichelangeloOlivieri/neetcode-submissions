class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        """
        1) nums = [13, 2, 13] -> [13]
        2) Brute Force, Array problem
        """
        
        res = []
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count

        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res

        """
        3) nums = [1], threshold = 0, freq = {1 : 1} -> [1]
        4) Time complexity O(n), where n = len(nums); space complexity O(n)
        """