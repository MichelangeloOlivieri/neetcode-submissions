class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if not temperatures:
            return []

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                last_index = stack.pop()
                res[last_index] = i - last_index

            stack.append(i)

        return res