from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # transitions = defaultdict(list)
        templates = defaultdict(list)
        wordList.append(beginWord)
        n = len(wordList)
        m = len(beginWord)
        
        foundEnd = False
        for word in wordList:
            if word == endWord:
                foundEnd = True
            for i in range(m):
                templateS = word[:i] + "_" + word[i + 1:]
                templates[templateS].append(word)
        if not foundEnd:
            return 0
        # use bfs, if we ever see a word again, ignore cause we already saw best
        # way to get to it from start
        
        # start at 0 since when we first pop we increment
        startQ = [beginWord]
        startSeen = {beginWord: 1}
        endQ = [endWord]
        endSeen = {endWord:1}
        # print(transitions)
        self.ans = float('inf')
        
        def moveQ(q, seen, otherSeen):
            newQ = []
            for val in q:
                dist = seen.get(val)
                if val in otherSeen:
                    # subtract 1 because we double count since we double count the overlap
                    self.ans = min(self.ans, dist + otherSeen.get(val) - 1)
                    return newQ
                for i in range(m):
                    tempS = val[:i] + "_" + val[i + 1:]
                    for word in templates.get(tempS, []):
                        if word in otherSeen:
                            self.ans = min(self.ans, dist + otherSeen.get(word))
                        elif word not in seen:
                            seen[word] = dist + 1
                            newQ.append(word)
            return newQ
        
        while startQ and endQ and self.ans == float('inf'):
            startQ = moveQ(startQ, startSeen, endSeen)
            if self.ans == float('inf'):
                endQ = moveQ(endQ, endSeen, startSeen)
        return self.ans if self.ans != float('inf') else 0
        
        
        
        
        
        
        
                        
                
        
        