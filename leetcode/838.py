from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        answer = list(dominoes)
        visited = [-1] * len(dominoes)
        queue = deque()
        for i, dominoe in enumerate(dominoes):
            if dominoe == "L":
                queue.append((i, "L"))
                visited[i] = 0
            if dominoe == "R":
                queue.append((i, "R"))
                visited[i] = 0
        
        cur_depth = 0
        while queue:
            cur_depth += 1
            for _ in range(len(queue)):
                cur_idx, cur_dir = queue.popleft()

                if cur_dir == "L":
                    if cur_idx-1 < 0:
                        continue

                    if answer[cur_idx-1] == ".":
                        answer[cur_idx-1] = "L"
                        visited[cur_idx-1] = cur_depth
                        queue.append((cur_idx-1, "L"))
                    elif answer[cur_idx-1] == "R":
                        if visited[cur_idx-1] == cur_depth:
                            answer[cur_idx-1] = "."

                elif cur_dir == "R":
                    if cur_idx+1 >= len(dominoes):
                        continue

                    if answer[cur_idx+1] == ".":
                        answer[cur_idx+1] = "R"
                        visited[cur_idx+1] = cur_depth
                        queue.append((cur_idx+1, "R"))

        return ''.join(answer)