class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        R = deque()
        D = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r_turn = R.popleft()
            d_turn = D.popleft()

            if r_turn < d_turn:
                R.append(r_turn + len(senate))
            else:
                D.append(d_turn + len(senate))

        return "Radiant" if R else "Dire"

        """
        - Time complexity O(n), where n = len(senate)
        - Space complexity O(n)
        """