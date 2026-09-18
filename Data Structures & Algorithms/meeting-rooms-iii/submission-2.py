class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        if not meetings or not meetings[0]:
            return 0
        
        meetings.sort()
        rooms_heap = [i for i in range(n)]
        min_heap = [] 
        count = [0] * n
        
        for start, end in meetings:

            while min_heap and start >= min_heap[0][0]:
                _, room = heapq.heappop(min_heap)
                heapq.heappush(rooms_heap, room)
            
            if rooms_heap:
                room = heapq.heappop(rooms_heap)
                heapq.heappush(min_heap, (end, room))
            else:
                end_time, room = heapq.heappop(min_heap)
                heapq.heappush(min_heap, (end_time + (end - start), room))
                
            count[room] += 1
            
        return count.index(max(count))

        """
        - Time complexity O(n * log(n) + m * log(m)), where m = len(meetings)
        - Space complexity O(n)
        """