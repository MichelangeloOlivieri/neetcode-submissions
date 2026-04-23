from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0  # Orologio globale
        self.tweets = defaultdict(list)  # Ora è una LISTA di tuple [tempo, tweetId]
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Usiamo il tempo negativo così il Min-Heap nativo di Python agisce da Max-Heap
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        # Un trucco elegante: aggiungiamo temporaneamente l'utente stesso ai suoi followees
        self.followees[userId].add(userId)
        
        # Riempiamo l'heap con IL TWEET PIÙ RECENTE di ogni persona seguita
        for followeeId in self.followees[userId]:
            if followeeId in self.tweets:
                # Prendiamo l'ultimo tweet della lista (il più recente)
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                # Inseriamo: [tempo, tweetId, chi_lo_ha_scritto, indice_precedente]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
                
        # Estraiamo fino a 10 tweet
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # Se l'utente che ha scritto questo tweet ne ha altri più vecchi, 
            # peschiamo il successivo e lo mettiamo nell'heap
            if index >= 0:
                next_count, next_tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [next_count, next_tweetId, followeeId, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Usiamo discard per prevenire il KeyError!
        self.followees[followerId].discard(followeeId)