class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if not nums:
            return 0

        curr = None
        count = 0

        for n in nums:
            if curr == None:
                curr = n
                count += 1
            else:
                if curr == n:
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        curr = None

        return curr

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """