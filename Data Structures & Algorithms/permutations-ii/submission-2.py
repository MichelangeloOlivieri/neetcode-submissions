class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        nums.sort()
        n = len(nums)
        visited = [False] * n
        res = []

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(n):
                if visited[i]:
                    continue
                if (i - 1 >= 0 and 
                    nums[i - 1] == nums[i] and 
                    not visited[i - 1]):
                        continue

                visited[i] = True
                curr.append(nums[i])
                backtrack(curr)
                visited[i] = False
                curr.pop()

        backtrack([])
        return res

        """
        Time complexity O(n! * n), where n = len(nums); space complexity O(n)
        """  