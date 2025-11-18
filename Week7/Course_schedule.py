from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a) 
            in_degree[a] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while queue:
            cur = queue.popleft()
            result.append(cur)
            for neighbor in adj[cur]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []
