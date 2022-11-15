class Node:
    def __init__(self):
        self.children = {}
        self.val = ""
        self.isWord = False
    
    def search(self, word, idx):
        """
        Searchs for word in current node and its children
        starting from the given index
        """
        if not self.val and idx == len(word):
            return self.isWord
        # iterate through value at node, return False
        # if discrepancy is found
        for i, char in enumerate(self.val):
            wordIdx = idx + i
            if wordIdx == len(word) or word[wordIdx] != char:
                return False
        if len(self.val) + idx == len(word):
            return self.isWord
        # if more of word left, check appropriate child node
        nextLetter = word[len(self.val) + idx]
        if nextNode:= self.children.get(nextLetter):
            return nextNode.search(word, idx + len(self.val) + 1)
        return False

    def prefixSearch(self, word, idx):
        """
        Similar to regular search but we only care if we have a path
        in the tree that includes all of the word from the given index
        """
        if len(word) == idx:
            return True
        for i, char in enumerate(self.val):
            wordIdx = idx + i
            if wordIdx == len(word):
                return True
            if word[wordIdx] != char:
                return False
        if len(self.val) + idx == len(word):
            return True
        nextLetter = word[len(self.val) + idx]
        if nextNode := self.children.get(nextLetter):
            return nextNode.prefixSearch(word, idx + len(self.val) + 1)
        return False
    
    def insert(self, word, idx):
        """
        Inserts a new word into the node and its children. To maintain
        the space-optimized structure, some rearranging might be neccessary.
        The problem is broken up into cases.
        """
        # Case 1: We are at the end of the word
        if idx == len(word):
            if not self.val:
                self.isWord = True
            
            # If there is a value at this node, we have to split
            # the node into 2
            else:
                changedPrevNode = Node()
                changedPrevNode.children = self.children
                changedPrevNode.isWord = self.isWord
                changedPrevNode.val = self.val[1:]

                self.children = {self.val[0]: changedPrevNode}
                self.val = ""
                self.isWord = True
                
        elif not self.val:
            if child:= self.children.get(word[idx]): 
                return child.insert(word, idx + 1)
            nextNode = Node()
            self.children[word[idx]] = nextNode
            nextNode.isWord = True
            nextNode.val = word[idx + 1:]   
        
        elif self.val[0] != word[idx]:
            changedPrevNode = Node()
            changedPrevNode.children = self.children
            changedPrevNode.isWord = self.isWord
            changedPrevNode.val = self.val[1:]
            self.children = {self.val[0]: changedPrevNode}
            self.val = ""
            self.isWord = False
            nextNode = Node()
            nextNode.val = word[idx + 1:]
            nextNode.isWord = True
            self.children[word[idx]] = nextNode
        
        else:
            sharedUpTo = 0
            while word[idx + sharedUpTo] == self.val[sharedUpTo]:
                sharedUpTo += 1
                if len(word) == sharedUpTo + idx or len(self.val) == sharedUpTo:
                    break
            newVal = word[idx: idx + sharedUpTo]
            if sharedUpTo + idx == len(word) and sharedUpTo == len(self.val):
                self.isWord = True
            
            elif sharedUpTo + idx == len(word):
                changedPrevNode = Node()
                changedPrevNode.children = self.children
                changedPrevNode.isWord = self.isWord
                changedPrevNode.val = self.val[sharedUpTo + 1:]
                self.children = {self.val[sharedUpTo]: changedPrevNode}
                self.val = word[idx: ]
                self.isWord = True  
            
            elif sharedUpTo == len(self.val):
                nextLetter = word[idx + sharedUpTo]
                if child:= self.children.get(nextLetter):
                    return child.insert(word, idx + sharedUpTo + 1)
                nextNode = Node()
                self.children[nextLetter] = nextNode
                nextNode.isWord = True
                nextNode.val = word[idx + sharedUpTo + 1:]
            
            else:
                changedPrevNode = Node()
                changedPrevNode.children = self.children
                changedPrevNode.isWord = self.isWord
                changedPrevNode.val = self.val[sharedUpTo + 1:]
                self.children = {self.val[sharedUpTo]: changedPrevNode}
                self.val = newVal
                self.isWord = False

                nextNode = Node()
                nextNode.val = word[idx + sharedUpTo + 1:]
                nextNode.isWord = True
                self.children[word[idx + sharedUpTo]] = nextNode             
            
                
class Trie:     
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if child:= self.root.children.get(word[0]):
            return child.insert(word, 1)
        nextNode = Node()
        self.root.children[word[0]] = nextNode
        nextNode.isWord = True
        nextNode.val = word[1:]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if child:= self.root.children.get(word[0]):
            return child.search(word, 1)
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if child:= self.root.children.get(prefix[0]):
            return child.prefixSearch(prefix, 1)
        return False