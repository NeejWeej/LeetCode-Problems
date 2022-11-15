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
        # iterate through value at node
        # return False if discrepancy is found
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
        # iterate through value at node
        # return False if discrepancy is found
        for i, char in enumerate(self.val):
            wordIdx = idx + i
            if wordIdx == len(word):
                return True
            if word[wordIdx] != char:
                return False
        if len(self.val) + idx == len(word):
            return True
        # if more of word left, check appropriate child node
        nextLetter = word[len(self.val) + idx]
        if nextNode:= self.children.get(nextLetter):
            return nextNode.prefixSearch(word, idx + len(self.val) + 1)
        return False
    
    def splitNode(self, splitIdx, wordStatus):
        """
        Splits the current node at a given index
        of its value, in-place. The current node spawns
        a child node that will inherit its children and
        "isWord" status, as well as all of the value 
        after the splitIdx. The current node's value becomes
        the original value before the splitIdx, it only has
        one child, which is the newly created child node, and
        its "isWord" status is set to wordStatus
        """
        changedPrevNode = Node()
        changedPrevNode.children = self.children
        changedPrevNode.isWord = self.isWord
        changedPrevNode.val = self.val[splitIdx + 1:]
        self.children = {self.val[splitIdx]: changedPrevNode}
        self.val = self.val[:splitIdx]
        self.isWord = wordStatus
        
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
            # the node
            else:
                self.splitNode(0, True)
        
        # Case 2: Not at the end of the word, but there is no value at this node
        elif not self.val:
            if child:= self.children.get(word[idx]): 
                return child.insert(word, idx + 1)
            nextNode = Node()
            self.children[word[idx]] = nextNode
            nextNode.isWord = True
            nextNode.val = word[idx + 1:]   
        
        # Case 3: We have a value and a word, we see up to which point
        # they align
        else:
            sharedUpTo = 0
            while word[idx + sharedUpTo] == self.val[sharedUpTo]:
                sharedUpTo += 1
                if len(word) == sharedUpTo + idx or len(self.val) == sharedUpTo:
                    break
                    
            if sharedUpTo + idx == len(word) and sharedUpTo == len(self.val):
                self.isWord = True
            
            # We have finished all of the word
            # we split the node
            elif sharedUpTo + idx == len(word):
                self.splitNode(sharedUpTo, True)
            
            # We have not finished the word, so we have
            # to look towards the children
            elif sharedUpTo == len(self.val):
                nextLetter = word[idx + sharedUpTo]
                if child:= self.children.get(nextLetter):
                    return child.insert(word, idx + sharedUpTo + 1)
                nextNode = Node()
                self.children[nextLetter] = nextNode
                nextNode.isWord = True
                nextNode.val = word[idx + sharedUpTo + 1:]
            
            # we have finished neither the word nor the
            # value, so we must split and create a new child
            # node that stores the rest of the word past
            # the shared portion
            else:
                self.splitNode(sharedUpTo, False)
                nextLetter = word[idx + sharedUpTo]
                nextNode = Node()
                nextNode.val = word[idx + sharedUpTo + 1:]
                nextNode.isWord = True
                self.children[nextLetter] = nextNode             
            
                
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