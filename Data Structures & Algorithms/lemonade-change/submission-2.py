class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        """
        1) bills = [5, 10, 20] -> False
        bills = [5, 10, 5, 20] -> True
        2) Array
        """

        if not bills:
            return False

        cash = {5 : 0, 10 : 0, 20 : 0}

        for i in range(len(bills)):
            pay = bills[i]

            if pay == 5:
                cash[5] += 1

            elif pay == 10:
                if cash[5] == 0:
                    return False
                else:
                    cash[5] -= 1
                    cash[10] += 1

            else:
                if cash[5] == 0:
                    return False
                else:
                    if cash[10] > 0:
                        cash[5] -= 1
                        cash[10] -= 1
                        cash[20] += 1
                    elif cash[5] >= 3:
                        cash[5] -= 3
                        cash[20] -= 1
                    else: 
                        return False

        return True

        """
        3) bills = [5, 10, 20]:
        - pay = 5: cash = {5 : 1, 10 : 0, 20 : 0}
        - pay = 10: cash = {5 : 0, 10 : 1, 20 : 0}
        - pay = 20: False
        bills = [5, 10, 5, 20]:
        - pay = 5: cash = {5 : 1, 10 : 0, 20 : 0}
        - pay = 10: cash = {5 : 0, 10 : 1, 20 : 0}
        - pay = 5: cash = {5 : 1, 10 : 1, 20 : 0}
        - pay = 20: cash = {5 : , 10 : 0, 20 : 1}
        4) Time complexity O(n), where n = len(bills); space complexity O(1)
        """