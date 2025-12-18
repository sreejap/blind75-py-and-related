class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        queue = deque()
        
        adjList = [[] for _ in range(numCourses)] # correct syntax

        for pq in prerequisites:
            adjList[pq[1]].append(pq[0]) # we want to say 0 → 1 for [1,0] where 1 requires 0

            indegree [pq[0]] += 1 

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        nodes_visited = 0
        while queue:
            course = queue.popleft()
            nodes_visited += 1

            for neighbor in adjList[course]:
                indegree [neighbor] -= 1

                if indegree[neighbor] == 0 :
                    queue.append(neighbor)                
        
        return nodes_visited == numCourses
