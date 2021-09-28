class Solution:
    import collections
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        is_prereq = collections.defaultdict(list)
        prereq_count = {}
        for course, prereq in prerequisites:
            is_prereq[prereq].append(course)
            prereq_count[course] = prereq_count.get(course, 0) + 1
        stack = []
        for i in range(numCourses):
            if i not in prereq_count:
                stack.append(i)
        ans = []
        
        while stack:
            cur = stack.pop()
            ans.append(cur)
            for course in is_prereq.get(cur, []):
                prereq_count[course] -= 1
                if prereq_count.get(course) == 0:
                    stack.append(course)
        return ans if len(ans) == numCourses else []
        