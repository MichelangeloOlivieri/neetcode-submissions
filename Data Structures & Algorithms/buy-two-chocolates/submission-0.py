class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        """
        1) prices = [3, 4, 2], money = 4 -> 1
                           ^   
            prices = [3, 1, 2], money = 2 -> 2
        2) Sort and take the least expensive ones, or use buckets, for loop with two variables
        """

        if not prices or len(prices) <= 1:
            return money

        first = float('inf')
        second = float('inf')
        for p in prices:
            if p < first:
                first = p
            if first < second:
                first, second = second, first

        total = first + second
        return money - total if total <= money else money

        """
        - Time complexity O(n), where n = len(prices)
        - Space complexity O(1)
        """