class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        """
        1)  asteroids = [4, -1, -3, 3, -2] -> [4, 3, 3]
            asteroids = [4, 3, -3] -> [4]
            asteroids = [-4, 3] -> [-4, 3]
        2) Stack solution
        """ 

        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = stack[-1] + a
                if diff > 0:
                    a = 0
                elif diff == 0:
                    a = 0
                    stack.pop()
                else:
                    stack.pop()
            if a:
                stack.append(a)

        return stack

        """
        3) asteroids = [10, 4, -5] -> stack = [10, -5]
        4) Time complexity O(n), where n = len(asteroids); space complexity O(n)
        """