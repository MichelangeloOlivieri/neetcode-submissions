class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # soluzione ottimizzata

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        """
        COMMENTO PRIMA CHE GUARDASSI LA SOLUZIONE
        1) Devo gestire casi in cui target < position[i] per qualche i? Esempio per vedere se 
        ho capito: target = 10; position = [5, 3, 1, 2]; speed = [1, 0.00000001, 10, 4]; 
        time_real = [5, +inf, 1, 2]; time_problem = [5, +inf, +inf, +inf]
        2) Se posso ordinare position il problema diventa molto più semplice; una car fleet è 
        individuata dal tempo in cui arriva; quindi basta raggruppare le auto in base all'orario
        in cui arrivano, tenendo però conto del fatto che un auto che parte più indietro non può
        superare la successiva e vi si "attacca"; sto usando uno stack in cui inserisco le 
        macchine in base a chi arriva prima e correggo il tempo se una macchina che è partita 
        più indietro è arrivata prima secondo il time_real -> mi arrendo
        """



                 
