class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        parent = list(range(n))
        parent[firstPerson] = 0
        size = [1] * n
        size[0] = 2

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        meetings.sort(key=lambda e : e[2])
        i = 0

        while i < len(meetings):
            j = i

            while j < len(meetings) and meetings[j][2] == meetings[i][2]:
                a = find(meetings[j][0])
                b = find(meetings[j][1])
                if a != b:
                    if size[b] > size[a]:
                        a, b = b, a 
                    parent[b] = a
                    size[a] += size[b]
                j += 1

            root = find(0)
            for at in range(i, j):
                for v in meetings[at][:2]:
                    if find(v) != root:
                        parent[v] = v
                        size[v] = 1

            i = j

        root = find(0)
        return [v for v in range(n) if find(v) == root]

        """
        - Time complexity O(m * log(m) + n), where m = len(meetings)
        - Space complexity O(n)
        """
