class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # Conterrà solo gli INDICI

        for i in range(len(temperatures)):
            # "Finché lo stack NON è vuoto E la temperatura attuale è maggiore 
            # di quella all'indice salvato in cima allo stack..."
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last_index = stack.pop() # Estraiamo l'indice
                result[last_index] = i - last_index # Calcoliamo la distanza
            
            # In ogni caso, a fine giro aggiungiamo l'indice attuale
            stack.append(i)

        return result