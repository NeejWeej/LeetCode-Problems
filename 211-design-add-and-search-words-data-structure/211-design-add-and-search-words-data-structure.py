class Node:
    
    def __init__(self, children, isWord=False):
        self.isWord = isWord
        self.children = children
    
    def addWord(self, word):
        if len(word) == 0:
            self.isWord = True
            return
        c = word[0]
        if c in self.children:
            self.children.get(c).addWord(word[1:])
        else:
            new_node = Node({})
            self.children[c] = new_node
            new_node.addWord(word[1:])
    
    def search(self, word):
        if len(word) == 0:
            return self.isWord
        next_char = word[0]
        if next_char == '.':
            for c, node in self.children.items():
                if node.search(word[1:]):
                    return True
            return False
        if next_char not in self.children:
            return False
        node = self.children.get(next_char)
        return node.search(word[1:])
            
class WordDictionary:

    def __init__(self):
        self.root = Node({})

    def addWord(self, word: str) -> None:
        self.root.addWord(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)