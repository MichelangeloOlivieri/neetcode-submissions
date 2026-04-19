class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        visti = set()

        for integer in nums:
            if integer in visti:
                return True
            else: 
                visti.add(integer)
        
        return False


        # nums = [1, 2, 3, 3]
        # dictionary = {"1" : "1", "2": "1", "3": "2"} ?
        # flag = True


        