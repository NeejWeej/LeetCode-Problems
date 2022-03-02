class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        layer = []
        courses = {i:[0, set()] for i in range(numCourses)}
        for adv, pq in prerequisites:
            courses[adv][0] = courses[adv][0] + 1
            courses[pq][1].add(adv)
        for course, info in courses.items():
            if info[0] == 0:
                layer.append(course)
                
        courses_taken = 0
        while layer:
            new_layer = []
            for course in layer:
                courses_taken += 1
                for future_course in courses[course][1]:
                    cur_count = courses[future_course][0]
                    courses[future_course][0] = cur_count - 1
                    if cur_count == 1:
                        new_layer.append(future_course)
            layer = new_layer
        return courses_taken == numCourses
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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