class Solution:
    def intToRoman(self, num: int) -> str:

        res = []
        to_roman = {
            1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX", 
            10 : "X", 20 : "XX", 30 : "XXX", 40 : "XL", 50 : "L", 60 : "LX", 70 : "LXX", 80 : "LXXX", 90 : "XC", 
            100 : "C", 200 : "CC", 300 : "CCC", 400 : "CD", 500 : "D", 600 : "DC", 700 : "DCC", 800 : "DCCC", 900 : "CM",
            1000 : "M", 2000 : "MM", 3000 : "MMM"
        }

        count = 0        
        while num > 0:
            digit = num % 10
            roman_digit = to_roman[digit * 10**count]
            res.append(roman_digit)
            num //= 10
            count += 1

        res.reverse()
        return "".join(res)

"""
- Time complexity: O(log_10(num)).
- Space complexity: O(log_10(num)) for output result.
"""