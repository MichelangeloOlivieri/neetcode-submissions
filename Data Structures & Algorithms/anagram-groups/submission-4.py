class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            group[tuple(count)].append(s)

        return [group[i] for i in group]

"""
- Time complexity: O(n), where n = Sum({len(s) | s in strs}).
- Space complexity: O(n).
"""