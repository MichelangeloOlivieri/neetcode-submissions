class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # mio tentativo

        """
        1) Dobbiamo supporre che len(s2) > len(s1), altrimenti il problema non ha senso; per il
        resto il problema mi sembra ben posto
        2) - Tentativo 1: controllare tutte le possibili sottostringhe con due cicli innestati 
        dà complessità O((n - k)klog(k)), dove n = len(s2), k = len(s1).
        - Tentativo 2: scorrere un indice, creare un dizionario per la stringa che ottengo di 
        lunghezza la lunghezza della sottostringa cercata, e confrontarlo con il dizionario di
        s1; se sono uguali ok; se no elimino tutto fino all'ultimo carattere diverso in qualche
        modo che non so
        """

        s1 = "".join(sorted(s1))

        for i in range(len(s2) - len(s1) + 1):
            
            temp = s2[i: i + len(s1)]
            temp = "".join(sorted(temp))

            if temp == s1:
                return True
        
        return False

        """
        """


        