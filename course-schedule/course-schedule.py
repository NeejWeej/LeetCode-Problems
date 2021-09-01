class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        is_prereq = collections.defaultdict(list)
        has_prereq = collections.defaultdict(int)
        for p in prerequisites:
            is_prereq[p[1]].append(p[0])
            has_prereq[p[0]] += 1
        start = []
        for c in range(numCourses):
            if has_prereq[c] == 0:
                start.append(c)
        count = 0
        visited = set()
        while start:
            curr_class = start.pop()
            count += 1
            for c in is_prereq[curr_class]:
                if c in visited:
                    continue
                has_prereq[c] -= 1
                if has_prereq.get(c) == 0:
                    visited.add(c)
                    start.append(c)          
        return True if count == numCourses else False