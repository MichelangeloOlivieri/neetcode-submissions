class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # tentativo mio

        """
        1) Assumo che le operazioni siano sempre ben definite? Esempio? non so cos'è (NDR: ho
        guardato esempi di neetcode perché non avevo idea di che cosa si stesse parlando) Assumo
        anche che l'ordine sia sempre rispettato e che non ci siano errori dovuti a inserimento
        di dati errati
        2) - Soluzione 1: usare uno stack per metterci i vari numeri che compaiono di volta in
        volta, fare l'operazione e poi rimuoverli dallo stack e andare avanti finché non si 
        finisce
        """

        stack = []
        operations = {'+', '-', '*', '/'}

        for s in tokens:

            if s not in operations:
                stack.append(s)
            else: 
                if s == '+':
                    res = int(stack[-2]) + int(stack[-1])
                if s == '-':
                    res = int(stack[-2]) - int(stack[-1])
                if s == '*':
                    res = int(stack[-2]) * int(stack[-1])
                if s == '/':
                    res = int(stack[-2]) / int(stack[-1])
                
                stack.pop()
                stack.pop()
                stack.append(res)

        return int(stack[0])

        """
        3) Dry run: - tokens = ["1", "2", "+", "5", "*", "3", "/"]
        - stack = ["1", "2"]; s = "+"; res = 3; stack = [3];
        - stack = [3, "5"]; s = "*"; res = 15; stack = [15]; etx
        4) Complessità temporale O(n); complessità spaziale O(1) (perché ogni volta elimino
        gli elementi, quindi lo stack è sempre lungo al massimo 2)
        """

