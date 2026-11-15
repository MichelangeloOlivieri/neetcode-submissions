class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counts = [0] * 1001
        for value in nums:
            counts[value] += 1
        answer = 1
        for start in range(1, k + 1):
            skip, take = 1, 0
            for value in range(start, 1001, k):
                choices = (1 << counts[value]) - 1
                skip, take = skip + take, skip * choices
            answer *= skip + take
        return answer - 1
