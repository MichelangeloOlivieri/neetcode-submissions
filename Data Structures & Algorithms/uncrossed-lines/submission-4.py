class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        1) nums1 = [2, 2]
        nums2 = [2, 2, 1]

        nums1 = [2, 3, 3]
        nums2 = [3, 3, 2, 1]
        2) DP
        """

        if not nums1 or not nums2:
            return 0

        index = defaultdict(deque)
        for i, n in enumerate(nums2):
            index[n].append(i)
            
        memo = {}

        def dfs(i, j):
            if i == len(nums1):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            assign = 0
            n = nums1[i]
            q = deque()

            next_j = -float('inf')
            while index[n] and next_j <= j:
                next_j = index[n].popleft()
                q.append(next_j)
            if next_j > j:
                assign = 1 + dfs(i + 1, next_j)
            while q:
                index[n].appendleft(q.pop())

            skip = dfs(i + 1, j)
            memo[(i, j)] = max(assign, skip)
            return memo[(i, j)]

        return dfs(0, -1)

        """
        (1, -1) -> (2, 0) -> (3, 1) -> (4, 2)
        """

        """
        - Time complexity O(m * n**2), where m = len(nums1) and n = len(nums2)
        - Space complexity O(m + n)
        """