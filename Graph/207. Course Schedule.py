class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - use DFS
        - hasmap to represent if they are prerequisites
        - empty list means empty prerequisite 
        - 
        """
        #map each numcourses to prerequisite list 
        preMap = { i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        #visitSet = all courses along the current dfs path
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                #detect loop cause we visit course twice
                return False
            if preMap[course] == []:
                return True
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):return False
        return True
            
