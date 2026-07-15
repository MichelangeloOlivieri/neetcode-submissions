class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        if not tickets:
            return []

        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)

        for u in graph:
            graph[u].sort(reverse=True)

        res = []

        def dfs(airport):
            while graph[airport]:
                dest = graph[airport].pop()
                dfs(dest)

            res.append(airport)

        dfs("JFK")
        return res[::-1]