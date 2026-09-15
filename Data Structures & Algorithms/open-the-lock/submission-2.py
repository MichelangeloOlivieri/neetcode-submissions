class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:

        locked = set(deadends)
        
        if "0000" in locked:
            return -1

        q = deque(["0000"])
        visited = set()
        visited.add("0000")
        turns = 0
        
        while q:
            for _ in range(len(q)):
                state = q.popleft()
                
                if state == target:
                    return turns
                
                for i in range(4):
                    digit = int(state[i])
                    
                    for move in (1, -1):
                        new_digit = str((digit + move) % 10)
                        new_state = state[: i] + new_digit + state[i + 1 :]
                        
                        if new_state not in locked and new_state not in visited:
                            visited.add(new_state)
                            q.append(new_state)
                            
            turns += 1
            
        return -1

        """
        - Time complexity O(n * a^n), where n is the number of slots and a is the cardinality of the alphabet
        - Space complexity O(a^n)
        """