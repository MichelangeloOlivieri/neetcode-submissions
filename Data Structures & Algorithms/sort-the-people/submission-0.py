class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        if not names:
            return []
        if not heights:
            return names

        names_heights = list(zip(names, heights))
        names_heights.sort(key=lambda x : x[1], reverse=True)

        return [name for name, _ in names_heights]

"""
- Time complexity: O(n * log(n)), where n = len(names).
- Space complesxity: O(n) for the output result.
"""