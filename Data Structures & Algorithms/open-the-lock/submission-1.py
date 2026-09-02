from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        # 1. Ottimizzazione RAM: Fondere deadends e visited in un unico Set.
        # Evita di allocare due Hash Table separate e annulla il doppio controllo 'in'.
        visited = set(deadends)
        
        if "0000" in visited:
            return -1
            
        visited.add("0000")
        q = deque(["0000"])
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
                        new_state = state[:i] + new_digit + state[i+1:]
                        
                        if new_state not in visited:
                            visited.add(new_state)
                            q.append(new_state)
                            
            turns += 1
            
        return -1

        """
        - Time complexity O(N * A^N), where N is the number of slots and A is the cardinality of the alphabet
        - Space complexity O(A^N)
        """