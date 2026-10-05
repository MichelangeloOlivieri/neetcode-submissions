class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        """
        1) ["bd", "ac"], order = "dfg...bacd"
        2) Hash Map
        """

        if not words:
            return False

        position = defaultdict(int)
        count = 0
        for c in order:
            count += 1
            position[c] = count

        def preceeds(s, t):
            i = 0
            while i < len(s) and i < len(t):
                if position[s[i]] < position[t[i]]:
                    return True
                if position[s[i]] > position[t[i]]:
                    return False
                i += 1

            if len(s) > len(t):
                return False

            return True

        for i in range(len(words) - 1):
            if not preceeds(words[i], words[i + 1]):
                return False

        return True

        """
        - Time complexity O(n), where n = #{characters}
        - Space complexity O(1)
        """       