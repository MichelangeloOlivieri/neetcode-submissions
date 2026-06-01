class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        """
        1) Empty input; example seen
        2) Create dictionaries to translate and multiply
        """

        if not num1 or not num2:
            return "0"
        if num1 == "0" or num2 == "0":
            return "0"

        letters_to_numbers = {
            "0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, 
            "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9
        }

        numbers_to_letters = {}
        for key, value in letters_to_numbers.items():
            numbers_to_letters[value] = key

        def toInteger(string):
            num = 0
            count = 0

            for i in range(len(string) - 1, -1, -1):
                if string[i] != "0":
                    num += letters_to_numbers[string[i]] * (10 ** count)
                    count += 1
                else:
                    count += 1

            return num

        def toString(num):

            string = collections.deque()
            
            while num > 0:
                digit = num % 10
                string.appendleft(numbers_to_letters[digit])
                num = num // 10

            return "".join(string)


        first = toInteger(num1)
        second = toInteger(num2)
        res = first * second

        return toString(res)

        """
        3) num1 = "101", num2 = "3"
        first = 101, second = 3 -> res = 303
        digit = 3 -> string = ["3"] -> num = 30 -> digit = 0 -> string = ["0", "3"]
        4) Time complexity O(m + n), where m = len(num1), n = len(num2); space 
        complexity O(m + n)
        """



