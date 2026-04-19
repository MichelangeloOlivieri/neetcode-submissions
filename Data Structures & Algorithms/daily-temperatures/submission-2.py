class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # tentativo mio

        """
        1) Esempio per vedere se ho capito: temperatures = [1, -2, 0, -4, -5, 10]; result = 
        = [5, 1, 3, 2, 1, 0]; nessuna domanda in particolare, il problema è ben posto
        2) - Soluzione 1: scorrere l'array con doppi indici e calcolare la distanza appena trovo
        un numero più grande -> tempo O(n^2)
        - Soluzione 2: ho visto l'hint e provo a implementarlo
        """

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            if not stack:
                stack.append(i)
            else: 
                last_index = stack[-1]

                while temperatures[last_index] < temperatures[i]:
                    result[last_index] = i - last_index
                    stack.pop()
                    if stack:
                        last_index = stack[-1]
                    else: 
                        break

                stack.append(i)

        return result

        """
        3) Dry run: - temperatures = [30, 38, 30, 36, 35, 40, 28]; stack = []
        - i = 0; stack = [0];
        - i = 1; last_index = 0; result[0] = 1; stack = []; stack = [38]
        - i = 2; last_index = 1; stack = [38, 30]
        - i = 3; last_index = 2; result[2] = 1; stack = [38]; last_index = 1; stack = [38, 36]
        4) Complessità temporale O(n); complessità spaziale O(n)
        """



        
        