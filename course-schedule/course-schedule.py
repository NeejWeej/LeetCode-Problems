class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        is_prereq = collections.defaultdict(list)
        has_prereq = collections.defaultdict(int)
        for p in prerequisites:
            is_prereq[p[1]].append(p[0])
            has_prereq[p[0]] += 1
        c2 = len(has_prereq.items())
        start = []
        # for c in range(numCourses):
        #     if has_prereq[c] == 0:
        #         start.append(c)
        for p in is_prereq.keys():
            if has_prereq[p] == 0:
                start.append(p)
        # count = 0
        visited = set()
        while start:
            curr_class = start.pop()
            # count += 1
            for c in is_prereq[curr_class]:
                if c in visited:
                    continue
                has_prereq[c] -= 1
                if has_prereq.get(c) == 0:
                    c2 -= 1
                    visited.add(c)
                    start.append(c)  
        # print(c2)
        return True if c2 == 0 else False