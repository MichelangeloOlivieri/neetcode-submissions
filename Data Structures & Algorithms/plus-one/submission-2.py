class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        """
        1) Empty input; example written; assuming no zero in the first entry
        2) Scan the array and do the math; check for "all 9's" case
        """
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
                
        return [1] + digits
        
        """
        3) Ok
        4) Time complexity O(n); space complexity O(1)
        """