class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if not temperatures:
            return []
        if len(temperatures) == 1:
            return [0]

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                last_index = stack.pop()
                res[last_index] = i - last_index

            stack.append(i)

        return res