class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        visti = set()

        for integer in nums:
            if integer in visti:
                return True
            else: 
                visti.add(integer)
        
        return False

        