class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        graph = defaultdict(list)
        graph[0].append((firstPerson, 0))
        graph[firstPerson].append((0, 0))
        max_time = 0

        meetings_set = [tuple(l) for l in meetings]
        meetings_set = set(meetings_set)

        for u, v, t in meetings_set:
            graph[u].append((v, t))
            graph[v].append((u, t))
            max_time = max(max_time, t)

        def bfs(node, time):
            q = deque()
            q.append(node)

            while q:
                curr = q.popleft()
                for nei, t in graph[curr]:
                    if nei not in can_share and time == t:
                        can_share.add(nei)
                        q.append(nei)

        can_share = set([0, firstPerson])
        time = 0

        for t in range(1, max_time + 1):
            for node in can_share.copy():
                bfs(node, t)

        return [i for i in can_share]

    """
    - Time complexity O(E + n + max_time), where E = len(meetings)
    - Space complexity O(E + n)
    """