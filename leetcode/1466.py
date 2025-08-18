class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        city = [[] for _ in range(n)]
        for connection in connections:
            city[connection[0]].append(connection[1])
            city[connection[1]].append(-connection[0])

        stack = [city[0]]
        visited = [True] + [False] * n
        neg_change = 0
        while stack:
            next_cities = stack.pop()
            for next_city in next_cities:
                if visited[abs(next_city)]:
                    continue
                else:
                    visited[abs(next_city)] = True
                if next_city < 0:
                    neg_change += 1
                stack.append(city[abs(next_city)])

        return n-neg_change-1
    
# Solved 28m14s