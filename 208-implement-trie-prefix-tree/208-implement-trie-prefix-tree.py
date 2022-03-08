class Node:
    def __init__(self):
        self.children = {}
        self.val = ""
        self.is_word = False
    
    def search(self, word):
        if not self.val and len(word) == 0:
            return self.is_word
        
        for idx, char in enumerate(self.val):
            if idx == len(word):
                return False
            if word[idx] != char:
                return False
            if idx == len(word) - 1 and idx == len(self.val) - 1:
                return self.is_word
        next_letter = word[len(self.val)]
        if next_letter not in self.children:
            return False
        nextt = self.children.get(next_letter)
        return nextt.search(word[len(self.val) + 1:])

    def prefixSearch(self, word):
        if len(word) == 0:
            return True
        for idx, char in enumerate(self.val):
            if idx == len(word):
                return True
            if word[idx] != char:
                return False
            if idx == len(word) - 1 and idx == len(self.val) - 1:
                return True
        next_letter = word[len(self.val)]
        if next_letter not in self.children:
            return False
        nextt = self.children.get(next_letter)
        return nextt.prefixSearch(word[len(self.val) + 1:])
    
    def insert(self, word):
        if len(word) == 0:
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
                if child == word[0]:
                    node.insert(word[1:])
                    return
            nextt = Node()
            self.children[word[0]] = nextt
            nextt.is_word = True
            nextt.val = word[1:]
        
        elif self.val[0] != word[0]:
            new_val_here = ""
            
            changed_prev_node = Node()
            changed_prev_node.children = self.children
            changed_prev_node.is_word = self.is_word
            changed_prev_node.val = self.val[1:]
            
            self.children = {self.val[0]: changed_prev_node}
            self.val = ""
            self.is_word = False
            
            nextt = Node()
            nextt.val = word[1:]
            nextt.is_word = True
            self.children[word[0]] = nextt
            
        else:
            share_up_to = 0
            while word[share_up_to] == self.val[share_up_to]:
                share_up_to += 1
                if len(word) == share_up_to or len(self.val) == share_up_to:
                    break
            
            new_val_here = word[:share_up_to]
            if share_up_to == len(word) and share_up_to == len(self.val):
                self.is_word = True
            
            elif share_up_to == len(word):
                changed_prev_node = Node()
                changed_prev_node.children = self.children
                changed_prev_node.is_word = self.is_word
                changed_prev_node.val = self.val[share_up_to + 1:]
                self.children = {self.val[share_up_to]: changed_prev_node}
                self.val = word
                self.is_word = True
            
            elif share_up_to == len(self.val):
                next_letter = word[share_up_to]
                for child, node in self.children.items():
                    if child == next_letter:
                        node.insert(word[share_up_to + 1:])
                        return
                nextt = Node()
                self.children[next_letter] = nextt
                nextt.is_word = True
                nextt.val = word[share_up_to + 1:]
                
            else:
                changed_prev_node = Node()
                changed_prev_node.children = self.children
                changed_prev_node.is_word = self.is_word
                changed_prev_node.val = self.val[share_up_to + 1:]
                self.children = {self.val[share_up_to]: changed_prev_node}
                self.val = new_val_here
                self.is_word = False

                nextt = Node()
                nextt.val = word[share_up_to + 1:]
                nextt.is_word = True
                self.children[word[share_up_to]] = nextt                
            
            
    

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
                node.insert(word[1:])
                return
        nextt = Node()
        self.root.children[word[0]] = nextt
        nextt.is_word = True
        nextt.val = word[1:]
        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word[0] not in self.root.children:
            return False
        nextt = self.root.children.get(word[0])
        return nextt.search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        word = prefix
        if word[0] not in self.root.children:
            return False
        nextt = self.root.children.get(word[0])
        return nextt.prefixSearch(word[1:])

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)