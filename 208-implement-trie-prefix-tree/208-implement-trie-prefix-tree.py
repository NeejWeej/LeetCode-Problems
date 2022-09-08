class Trie:

    def __init__(self):
        self.t = {}

    def insert(self, word: str) -> None:
        cur = self.t
        for char in word:
            cur[char] = cur.get(char, {})
            cur = cur.get(char)
        cur['#'] = True

    def search(self, word: str) -> bool:
        n = len(word)
        cur = self.t
        i = 0
        while i < n and cur:
            cur = cur.get(word[i], {})
            i += 1
        return i == n and '#' in cur

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        cur = self.t
        i = 0
        while i < n and cur:
            cur = cur.get(prefix[i], {})
            i += 1
        return i == n and cur
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)