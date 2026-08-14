class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        res = []
        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0

        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = n
                count1 += 1
            elif count2 == 0:
                cand2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        threshold = len(nums) // 3
        for c in set([cand1, cand2]):
            if c is not None and nums.count(c) > threshold:
                res.append(c)
        
        return res

        """
        Time complexity O(n), where n = len(nums); space complexity O(1)
        """