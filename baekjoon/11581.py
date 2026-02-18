'''
Level: S1
Time: 41m46s
'''
import sys
input = lambda: sys.stdin.readline().strip()


def solution(graph, visited, cur_node, N):
    if cur_node == N:
        return True
    
    for next_node in graph[cur_node]:
        if visited[next_node] == True:
            return False
        visited[next_node] = True
        if not solution(graph, visited, next_node, N):
            return False
        visited[next_node] = False

    return True


if __name__ == "__main__":
    N = int(input())

    graph = dict()
    for i in range(1, N):
        M = int(input())
        C = list(map(int, input().split()))
        graph[i] = C

    visited = [False] * (N+1)
    visited[1] = True
    print("NO CYCLE") if solution(graph, visited, 1, N) else print("CYCLE")    