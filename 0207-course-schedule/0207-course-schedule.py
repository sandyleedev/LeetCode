class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {course: [] for course in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            preMap[crs] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True