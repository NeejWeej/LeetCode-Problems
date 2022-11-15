class Node:
    def __init__(self):
        self.children = {}
        self.val = ""
        self.is_word = False
    
    def search(self, word, idx):
        if not self.val and idx == len(word):
            return self.is_word
        
        for i, char in enumerate(self.val):
            wordIdx = idx + i
            if wordIdx == len(word):
                return False
            if word[wordIdx] != char:
                return False
            if wordIdx == len(word) - 1 and i == len(self.val) - 1:
                return self.is_word
        nextLetter = word[len(self.val) + idx]
        nextNode = self.children.get(nextLetter)
        if not nextNode:
            return False
        return nextNode.search(word, idx + len(self.val) + 1)

    def prefixSearch(self, word, idx):
        if len(word) == idx:
            return True
        for i, char in enumerate(self.val):
            wordIdx = idx + i
            if wordIdx == len(word):
                return True
            if word[wordIdx] != char:
                return False
            if wordIdx == len(word) - 1 and i == len(self.val) - 1:
                return True
        next_letter = word[len(self.val) + idx]
        nextNode = self.children.get(next_letter)
        if not nextNode:
            return False
        return nextNode.prefixSearch(word, len(self.val) + idx + 1)
    
    def insert(self, word, idx):
        if idx == len(word):
            if not self.val:
                self.is_word = True
            else:
                changed_prev_node = Node()
                changed_prev_node.children = self.children
                changed_prev_node.is_word = self.is_word
                changed_prev_node.val = self.val[1:]

                self.children = {self.val[0]: changed_prev_node}
                self.val = ""
                self.is_word = True
                
        elif not self.val:
            for child, node in self.children.items():
                if child == word[idx]:
                    return node.insert(word, idx + 1)
            nextNode = Node()
            self.children[word[idx]] = nextNode
            nextNode.is_word = True
            nextNode.val = word[idx + 1:]   
        
        elif self.val[0] != word[idx]:
            new_val_here = ""
            changed_prev_node = Node()
            changed_prev_node.children = self.children
            changed_prev_node.is_word = self.is_word
            changed_prev_node.val = self.val[1:]
            self.children = {self.val[0]: changed_prev_node}
            self.val = ""
            self.is_word = False
            nextNode = Node()
            nextNode.val = word[idx + 1:]
            nextNode.is_word = True
            self.children[word[idx]] = nextNode
        
        else:
            share_up_to = 0
            while word[idx + share_up_to] == self.val[share_up_to]:
                share_up_to += 1
                if len(word) == share_up_to + idx or len(self.val) == share_up_to:
                    break
            new_val_here = word[idx: idx + share_up_to]
            if share_up_to + idx == len(word) and share_up_to == len(self.val):
                self.is_word = True
            
            elif share_up_to + idx == len(word):
                changed_prev_node = Node()
                changed_prev_node.children = self.children
                changed_prev_node.is_word = self.is_word
                changed_prev_node.val = self.val[share_up_to + 1:]
                self.children = {self.val[share_up_to]: changed_prev_node}
                self.val = word[idx: ]
                self.is_word = True  
            
            elif share_up_to == len(self.val):
                next_letter = word[idx + share_up_to]
                for child, node in self.children.items():
                    if child == next_letter:
                        return node.insert(word, idx + share_up_to + 1)
                nextNode = Node()
                self.children[next_letter] = nextNode
                nextNode.is_word = True
                nextNode.val = word[idx + share_up_to + 1:]
            
            else:
                changed_prev_node = Node()
                changed_prev_node.children = self.children
                changed_prev_node.is_word = self.is_word
                changed_prev_node.val = self.val[share_up_to + 1:]
                self.children = {self.val[share_up_to]: changed_prev_node}
                self.val = new_val_here
                self.is_word = False

                nextNode = Node()
                nextNode.val = word[idx + share_up_to + 1:]
                nextNode.is_word = True
                self.children[word[idx + share_up_to]] = nextNode             
            
                
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
        for child, node in self.root.children.items():
            if child == word[0]:
                node.insert(word, 1)
                return
        nextNode = Node()
        self.root.children[word[0]] = nextNode
        nextNode.is_word = True
        nextNode.val = word[1:]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word[0] not in self.root.children:
            return False
        nextNode = self.root.children.get(word[0])
        return nextNode.search(word, 1)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        word = prefix
        if word[0] not in self.root.children:
            return False
        nextt = self.root.children.get(word[0])
        return nextt.prefixSearch(word, 1)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)