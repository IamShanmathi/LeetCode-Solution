class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre_map = defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)
            
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False  # Cycle detected
            if not pre_map[course]:
                return True
                
            visiting.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            pre_map[course] = []  # Optimization: course is verified
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
                
        return True
        