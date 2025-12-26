graph = {
    0:[1,2],
    1:[0,3],
    2:[0,3],
    3:[1,2]
}

# DFS
def dfs(node, visited):
    if node in visited: return
    visited.add(node)
    for nei in graph[node]:
        dfs(nei, visited)

# BFS
from collections import deque
def bfs(start):
    q = deque([start])
    visited = set([start])
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
