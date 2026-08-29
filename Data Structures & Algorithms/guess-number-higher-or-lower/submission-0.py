# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        """
        1) n = 8, pick = 8 -> 3

        - l = 1, r = 8, mid = 4 -> guess(mid) = 1
        - l = 5, r = 8, mid = 6 -> guess(mid) = 1
        - l = 7, r = 8, mid = 7 -> guess(mid) = 1
        - l = 8, r = 8, mid = 8

        2) Binary Search
        """

        l = 1
        r = n

        while l <= r:
            mid = (l + r) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                l = mid + 1
            else:
                r = mid - 1

        return -1

        """
        - Time complexity O(log(n))
        - Space complexity O(n)
        """ 