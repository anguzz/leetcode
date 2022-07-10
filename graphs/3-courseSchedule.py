#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)} #map every course to empty list
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited= set()
        
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visited.remove(course)
            preMap[course]=[]  #set to empty incase we come across again will return true
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True
    
                
        
        
      
                
            
        
        
        
        
        
