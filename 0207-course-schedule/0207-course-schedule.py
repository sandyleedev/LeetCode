from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # key: pre-course, value: courses that can be taken after
        graph = defaultdict(list)

        # number of pre-courses of this specific course
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # queue of the courses whose indegree is 0
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        taken = 0

        while queue:
            cur = queue.popleft()
            taken += 1
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return taken == numCourses