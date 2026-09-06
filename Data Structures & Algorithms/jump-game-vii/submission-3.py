class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        if not s or s[-1] == "1":
            return False

        q = deque([0])
        furthest = 0

        while q:
            i = q.popleft()

            start = max(i + minJump, furthest + 1)
            end = min(i + maxJump, len(s) - 1)

            for j in range(start, end + 1):
                if s[j] == "0":
                    if j == len(s) - 1:
                        return True
                    q.append(j)

            furthest = i + maxJump    

        return False

        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(n)
        """