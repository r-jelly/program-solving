from collections import deque

V, E = list(map(int, input().split()))
K = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = list(map(int, input().split()))
    graph[u].append((v, w))

weight = [float('inf')] * (V+1)
weight[K] = 0

queue = deque([(K, 0)])
while queue:
    # print(queue)
    cur_node, cur_w = queue.popleft()

    for n, w in graph[cur_node]:
        # print(n, w)
        if cur_w+w < weight[n]:
            weight[n] = cur_w+w
            queue.append((n, weight[n]))

for i in range(1, V+1):
    print(weight[i])
'''
4 5
1
1 2 3
1 3 6
1 4 7
2 3 1
3 4 1
'''

'''
4 5
1
1 2 7
1 3 6
1 4 3
4 3 1
3 2 1
'''
import heapq

V, E = list(map(int, input().split()))
K = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = list(map(int, input().split()))
    graph[u].append((v, w))

distance = [float('inf')] * (V+1)
distance[K] = 0
visited = [False] * (V+1)

queue = [(0, K)]
while queue:
    cur_d, cur_node = heapq.heappop(queue)
    for v, w in graph[cur_node]:
        if visited[v]:
            continue
        if distance[cur_node] + w < distance[v]:
            distance[v] = distance[cur_node] + w
            heapq.heappush(queue, (distance[v], v))
    visited[cur_node] = True

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])