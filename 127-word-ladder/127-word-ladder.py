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
        # n = len(wordList)
        wl = len(wordList[0])
        q = set([beginWord])
        backwards = set([endWord])
        d = 1
        unvisited = set(wordList)
        b_unv = set(wordList)
        if endWord not in unvisited:
            return 0
        while q and backwards:
            # print(q, backwards, d)
            if len(q) > len(backwards):
                q, backwards, unvisited, b_unv = backwards, q, b_unv, unvisited
            next_layer = set()
            for cur in q:
                remove = []
                for word in unvisited:
                    if self.wordCompare(cur, word, wl):
                        if word in backwards:
                            return d + 1
                        remove.append(word)
                for word in remove:
                    unvisited.remove(word)
                    next_layer.add(word)
            q = next_layer
            d += 1
        return 0
                    