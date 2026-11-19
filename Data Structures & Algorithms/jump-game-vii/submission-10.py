class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        # BFS

        n = len(s)
        if s[n - 1] == "1":
            return False
        
        q = deque([0])
        furthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, furthest + 1)
            end = min(i + maxJump + 1, n)

            for j in range(start, end):
                if s[j] == "0":
                    if j == n - 1:
                        return True
                    q.append(j)
                    
            furthest = end - 1

        return False

    """
    - Time complexity: O(n), where n = len(s).
    - Space complexity: O(n).
    """