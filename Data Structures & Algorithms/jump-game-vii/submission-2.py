class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        """
        1) s = "01010", minJump = 2, maxJump = 4
        2) String, Dynamic Programming
        """

        if not s or s[-1] == "1":
            return False

        memo = {}
        memo[0] = True

        def dfs(i):
            if i == 0:
                return True
            if i in memo:
                return memo[i]

            can_reach = False
            for j in range(i - minJump, max(i - maxJump, 0) - 1, -1):
                if s[j] == "0":
                    can_reach = can_reach or dfs(j)
                    if can_reach:
                        break

            memo[i] = can_reach
            return memo[i]            

        return dfs(len(s) - 1)

        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(n)
        """