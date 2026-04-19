class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []
        if k >= len(nums):
            return nums

        res = []

        frequencies = {}
        for n in nums:
            frequencies[n] = 1 + frequencies.get(n, 0)

        classifica = [[] for i in range(len(nums) + 1)]
        for n in frequencies:
            classifica[frequencies[n]].append(n)

        for i in range(len(classifica) - 1, -1, -1):
            for n in classifica[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res
        
        

        
        