class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        """
        1) Empty input; example written
        2) Graph approach
        """

        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        nei = collections.defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
                
        visited = set([beginWord])
        q = collections.deque([(beginWord, 1)]) 

        while q:
            word, length = q.popleft()
            
            if word == endWord:
                return length
            
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                
                for neiWord in nei[pattern]:
                    if neiWord not in visited:
                        visited.add(neiWord)
                        q.append((neiWord, length + 1))
                        
        return 0

        """
        Time complexity O(n * m^2), where n = len(wordList) and m = len(beginWord); 
        space complexity O(n * m^2)
        """
        