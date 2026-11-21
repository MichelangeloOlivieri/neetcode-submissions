class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # if you can reach the goal, the current index becomes the new goal
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

"""
- Time complexity: O(n), where n = len(nums).
- Space complexity: O(1).
"""