class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        
        for u, v in tickets:
            graph[u].append(v)
        for u in graph:
            graph[u].sort(reverse=True)

        res = []
        stack = ["JFK"]

        while stack:
            curr = stack[-1]
            if graph[curr]:
                stack.append(graph[curr].pop())
            else:
                res.append(stack.pop())

        return res[::-1]

    """
    - Time complexity O(E * log(E) + V), where E = len(tickets) and V = #{airports}
    - Space complexity O(E + V)
    """