import sys
from collections import defaultdict

def solution1():
    def dfs(graph, visited, cur_node, weight):
        max_weight = weight
        for next_node, w in graph[cur_node]:
            if visited[next_node]:
                continue

            visited[next_node] = True
            next_weight = dfs(graph, visited, next_node, weight+w)
            if next_weight > max_weight:
                max_weight = next_weight
            visited[next_node] = False
        
        return max_weight

    N = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    
    for _ in range(N-1):
        n1, n2, w = list(map(int, sys.stdin.readline().split()))
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))

    visited = [False] * (N+1)
    max_weight = 0
    for i in range(1, N+1):
        visited[i] = True
        cur_weight = dfs(graph, visited, i, 0)
        if max_weight<cur_weight: max_weight=cur_weight
        visited[i] = False
    print(max_weight)


def solution3():
    def dfs(graph, visited, cur_node, weight):
        max_weight, max_node = weight, cur_node
        for next_node, w in graph[cur_node]:
            if visited[next_node]:
                continue

            visited[next_node] = True
            next_max_weight, next_max_node = dfs(graph, visited, next_node, weight+w)
            if next_max_weight > max_weight:
                max_weight = next_max_weight
                max_node = next_max_node
            visited[next_node] = False
        
        return max_weight, max_node

    N = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    
    for _ in range(N-1):
        n1, n2, w = list(map(int, sys.stdin.readline().split()))
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))

    visited = [False] * (N+1)

    visited[1] = True
    _, max_node = dfs(graph, visited, 1, 0)
    visited[1] = False
    visited[max_node] = True
    max_weight, _ = dfs(graph, visited, max_node, 0)
    print(max_weight)


def solution4():
    def dfs(graph, visited, cur_node, weight):
        stack = [(cur_node, weight)]
        max_weight, max_node = weight, cur_node

        while stack:
            cur_node, weight = stack.pop()
            if max_weight < weight:
                max_weight = weight
                max_node = cur_node

            for next_node, next_weight in graph[cur_node]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                stack.append((next_node, weight+next_weight))
        
        return max_weight, max_node

    N = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    
    for _ in range(N-1):
        n1, n2, w = list(map(int, sys.stdin.readline().split()))
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))

    visited = [False] * (N+1)
    visited[1] = True
    _, max_node = dfs(graph, visited, 1, 0)
    
    visited = [False] * (N+1)
    visited[max_node] = True
    max_weight, _ = dfs(graph, visited, max_node, 0)
    
    print(max_weight)

solution4()

# 1h34m25s