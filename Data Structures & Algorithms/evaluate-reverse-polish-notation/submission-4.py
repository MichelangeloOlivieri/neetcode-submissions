class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operations = {'+', '-', '*', '/'}

        for s in tokens:
            if s not in operations:
                # 1. È sicuramente un numero. Lo converto ORA e lo metto nello stack.
                stack.append(int(s)) 
            else: 
                # 2. Se finisco qui, è un operatore. 
                # Estraggo subito i due numeri (che ora SO essere già interi)
                b = stack.pop() # Secondo operando (quello più in alto)
                a = stack.pop() # Primo operando (quello sotto)
                
                # 3. Faccio l'operazione con elif
                if s == '+':
                    res = a + b
                elif s == '-':
                    res = a - b
                elif s == '*':
                    res = a * b
                elif s == '/':
                    # Mantengo int() qui per rispettare il troncamento verso lo zero di LeetCode
                    res = int(a / b) 
                    
                # 4. Rimetto il risultato (che è un intero) nello stack
                stack.append(res)

        return stack[0]