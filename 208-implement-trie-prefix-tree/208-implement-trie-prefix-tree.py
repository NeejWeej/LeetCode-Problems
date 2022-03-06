class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        if len(word) == 0:
            self.is_word = True
            return
        nextt = self.children.get(word[0], Node())
        self.children[word[0]] = nextt
        nextt.insert(word[1:])

    def search(self, word):
        if len(word) == 0:
            return self.is_word
        if word[0] not in self.children:
            return False
        nextt = self.children.get(word[0], Node())
        return nextt.search(word[1:])

    def prefixSearch(self, word):
        if len(word) == 0:
            return True
        if word[0] not in self.children:
            return False
        nextt = self.children.get(word[0], Node())
        return nextt.prefixSearch(word[1:])
class Trie:     
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.root.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.root.search(word)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.root.prefixSearch(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)