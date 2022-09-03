class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        best = 1
        words.sort(key = len, reverse=True)
        lengths = {word: 1 for word in words}
        n = len(words)
        
        def firstFewer(start):
            l = start
            r = n - 1
            wordLen = len(words[start]) - 1
            while l < r:
                mid = (l + r) // 2
                if len(words[mid]) > wordLen:
                    l = mid + 1
                else:
                    r = mid
            return l if len(words[l]) == wordLen else -1
        
        for idx,word in enumerate(words):
            startIdx = firstFewer(idx)
            if startIdx == -1:
                continue
            wordL = len(word)
            for i in range(startIdx, n):
                newW = words[i]
                if wordL - 1 != len(newW):
                    break
                for spot in range(wordL):
                    if newW == "".join(word[: spot] + word[spot + 1:]):
                        lengths[newW] = max(lengths.get(newW), 1 + lengths.get(word))
                        best = max(best, lengths[newW])
        return best
                    
                    
                
                
                
            
            