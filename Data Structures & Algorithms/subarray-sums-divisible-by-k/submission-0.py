class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix = {0 : 1}
        curr = 0
        res = 0

        for n in nums:
            curr += n
            mod_k = curr % k

            if mod_k in prefix:
                res += prefix[mod_k]

            prefix[mod_k] = prefix.get(mod_k, 0) + 1

        return res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(k)
        """
