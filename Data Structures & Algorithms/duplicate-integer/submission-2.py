class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dictionary = {}

        for integer in nums:
            if integer in dictionary:
                dictionary[integer] += 1
            else:
                dictionary[integer] = 1
            

        flag = False
        for integer in dictionary:
            if dictionary[integer] > 1:
                flag = True
                break
        
        return flag
                
        # nums = [1, 2, 3, 3]
        # dictionary = {"1" : "1", "2": "1", "3": "2"} ?
        # flag = True
        