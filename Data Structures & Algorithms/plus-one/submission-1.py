class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        """
        1) Empty input; example written; assuming no zero in the first entry
        2) Scan the array and do the math; check for "all 9's" case
        """
        
        if not digits:
            return 1

        res = deque()
        remainder = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + remainder
            if total != 10:
                res.appendleft(total)
                remainder = 0
            elif i != 0:
                res.appendleft(0)
                remainder = 1
            else:
                res.appendleft(0)
                res.appendleft(1)
        
        return list(res)

        """
        3) Ok
        4) Time complexity O(n); space complexity O(n)
        """