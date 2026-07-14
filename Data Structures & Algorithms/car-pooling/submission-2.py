class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # ==========================================
        # Clarifying Questions (Implicit):
        # 1. Are locations strictly between 0 and 1000? (Assume arbitrary bounds to build a robust SOTA solution).
        # 2. If a drop-off and a pick-up happen at the exact same location, do we drop off first? (Yes, to maximize available capacity).
        #
        # Algorithm Description:
        # Deconstruct trips into discrete atomic events (pickups and drop-offs), sort them chronologically (prioritizing drop-offs on ties), and simulate the passenger load linearly against the capacity constraint.
        # ==========================================

        if not trips:
            return True

        events = []
        for num_passengers, start_loc, end_loc in trips:
            events.append((start_loc, num_passengers))
            events.append((end_loc, -num_passengers))
            
        events.sort()

        current_passengers = 0
        for location, passenger_change in events:
            current_passengers += passenger_change
            if current_passengers > capacity:
                return False

        return True

        # ==========================================
        # Time Complexity: O(N log N) dominated by the sorting step, where N is the number of trips (2N events).
        # Space Complexity: O(N) to store the events.
        # ==========================================