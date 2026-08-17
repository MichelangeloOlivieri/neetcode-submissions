class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        """
        1) arr = [10, 9, 10, 18, 9, 10, 10] -> 3
        2) Array, DP 
        """

        if not arr:
            return 0

        dp = [1] * len(arr)
        sign = None

        j = 0
        for j in range(len(dp) - 2, -1, -1):
            if arr[j] != arr[j + 1]:
                dp[j] = 2
                if arr[j] > arr[j + 1]:
                    sign = True
                else:
                    sign = False
                break

        for i in range(j - 1, -1, -1):
            if arr[i] < arr[i + 1]:
                if sign:
                    dp[i] = 1 + dp[i + 1]
                else:
                    dp[i] = 2
                sign = False
            elif arr[i] > arr[i + 1]:
                if not sign:
                    dp[i] = 1 + dp[i + 1]
                else:
                    dp[i] = 2
                sign = True
            else:
                continue

        return max(dp)     

        """
        3) arr = [10, 9, 10, 18, 9, 10, 10]
        -> dp = [1, 1, 1, 1, 2, 1, 1], sign = None
        - j = 5 -> continue
        - j = 4 -> dp[4] = 2, sign = False -> break
        - i = 3 -> dp[3] = 3, sign = True
        - i = 2 -> dp[2] = 4, sign = False
        - i = 1 -> dp[1] = 2, sign = False
        - i = 0 -> dp[0] = 3, sign = True
        4) Time complexity O(n), where n = len(arr), space complexity O(n)
        """