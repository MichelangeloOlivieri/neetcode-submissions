class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # soluzione ottimizzata con BucketSort

        count = {}  # creo hash map delle frequenze
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]   # creo lista dei bucket indicizzata dalle frequenze
        for n, c in count.items():
            freq[c].append(n)

        res = []    # metto gli interi desiderati nella lista "res"
        for c in range(len(freq) - 1, 0, -1):
            for n in freq[c]:
                res.append(n)
                if len(res) == k:
                    return res


        

        
        