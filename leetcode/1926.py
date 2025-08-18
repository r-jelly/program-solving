class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        M, N = len(maze), len(maze[0])
        visited = [[False]*N for _ in range(M)]
        visited[entrance[0]][entrance[1]] = True

        stack = [(entrance, 0)]
        all_move = [[1,0], [-1,0], [0,1], [0,-1]]
        while stack:
            cur_point, cur_move = stack.pop(0)
            row, col = cur_point
            for dx, dy in all_move:
                if (0 <= row+dx < M) and (0 <= col+dy < N):
                    if visited[row+dx][col+dy]:
                        continue
                    visited[row+dx][col+dy] = True
                    if maze[row+dx][col+dy] != '+':
                        stack.append(([row+dx, col+dy], cur_move+1))
                elif row != entrance[0] or col != entrance[1]:
                    return cur_move
        return -1
                    
# Solved 13m52s