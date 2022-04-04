import collections
class Solution:
    def wordCompare(self, w1, w2, wl):
        diffs = 0
        for j in range(wl):
            if w1[j] != w2[j]:
                diffs += 1
                if diffs > 1:
                    break
        if diffs == 1:
            return True
        return False
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = collections.defaultdict(set)
        # n = len(wordList)
        wl = len(wordList[0])
        q = collections.deque([(beginWord, 1)])
        # visited = set([beginWord])
        unvisited = set(wordList)
        if endWord not in unvisited:
            return 0
        while q:
            cur, val = q.popleft()[:]
            if cur == endWord:
                return val
            remove = []
            for word in unvisited:
                if self.wordCompare(cur, word, wl):
                    remove.append(word)
            for word in remove:
                unvisited.remove(word)
                q.append((word, val + 1))
        return 0
                    