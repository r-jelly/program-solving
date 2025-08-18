class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        stack = [(0, rooms[0])]
        visited = [False] * len(rooms)
        while stack:
            num, keys = stack.pop()
            if visited[num]:
                continue
            
            visited[num] = True
            for key in keys:
                stack.append((key, rooms[key]))
        return all(visited)

# Solved 4m44s