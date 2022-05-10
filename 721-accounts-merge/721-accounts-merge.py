from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def get_parent(parents, start):
            # print('first '+start)
            path = []
            while parents.get(start):
                path.append(start)
                start = parents[start]
                # print(start)
            for p in path:
                parents[p] = start
            return start
        accs = {}
        acc_to_name = {}
        for name, *account in accounts:
            seen_person = False
            seen_a = set()
            for a in account:
                if a in accs:
                    seen_person = True
                    seen_a.add(a)
            if not seen_person:
                first = account[0]
                accs[first] = None
                acc_to_name[first] = name
                for acc in account:
                    if acc != first:
                        accs[acc] = first
            elif seen_person:
                first = next(iter(seen_a))
                p = get_parent(accs, first)
                for a in seen_a:
                    parent = get_parent(accs, a)
                    if parent != p:
                        accs[parent] = p
                for a in account:
                    if a != p:
                        accs[a] = p
        set_items = defaultdict(list)
        for a in accs:
            p = get_parent(accs, a)
            set_items[p].append(a)
        ans = [
            [acc_to_name.get(acc)] + sorted(it) 
            for acc,it in set_items.items()
            ]   
        # print(accs)
        return ans