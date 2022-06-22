class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
class Solution:
    from collections import defaultdict
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToOwner = {}
        idx = 0
        for name, *line in accounts:
            sameAs = {}
            newParent = Node(name)
            for email in line:
                if email in emailToOwner:
                    sameAs[emailToOwner[email]] = 1
                emailToOwner[email] = newParent
            sameAs.pop(newParent, "")
            count = 0
            for p in sameAs:
                count = 0
                while p.parent is not None and (p.parent != newParent):
                    temp = p
                    p = p.parent
                    temp.parent = newParent
                p.parent = newParent
        accounts = defaultdict(list)
        for email, parent in emailToOwner.items():
            while parent.parent is not None:
                parent = parent.parent
            accounts[parent].append(email)
        ans = []
        for p, emails in accounts.items():
            new = [p.name]
            new += sorted(emails)
            ans.append(new)
        return ans
        
                    
            