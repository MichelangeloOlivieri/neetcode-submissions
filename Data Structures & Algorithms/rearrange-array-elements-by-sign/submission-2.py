class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        m = len(nums)
        positives = []
        negatives = []

        for n in nums:
            if n > 0:
                positives.append(n)
            else:
                negatives.append(n)

        res = []

        for i in range(m // 2):
            res.append(positives[i])
            res.append(negatives[i])

        return res

"""
- Time complexity: O(n), where n = len(nums).
- Space complexity: O(1).
"""