class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                _, last_index = stack.pop()
                result[last_index] = i - last_index
            
            stack.append((temperatures[i], i))

        return result

        """
        - Time complexity O(n), where n = len(temperatures)
        - Space complexity O(n)
        """