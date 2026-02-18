# 0-1 BFS 풀이
# from collections import deque

# N, K = list(map(int, input().split()))
# visited = [False] * 200110

# def bfs():
#     queue = deque([(N, 0)])
#     visited[N] = True

#     while queue:
#         cur_node, cur_time = queue.popleft()
#         if cur_node == K:
#             return cur_time
        
#         if cur_node*2 < 100050:
#             if not visited[cur_node*2]:
#                 visited[cur_node*2] = True
#                 queue.appendleft((cur_node*2, cur_time))
        
#         for next_node in [cur_node-1, cur_node+1]:
#             if next_node>=0:
#                 if not visited[next_node]:
#                     visited[next_node] = True
#                     queue.append((next_node, cur_time+1))

# print(bfs())

# from collections import deque

# N, K = list(map(int, input().split()))

# visited = [False] * 200110
# queue = deque([(N, 0)])
# while queue:
#     cur_node, cur_time = queue.popleft()
#     if cur_node == K:
#         print(cur_time)
#         break

#     if cur_node*2 > 100050 or visited[cur_node*2]:
#         continue
#     else:
#         visited[cur_node*2] = True
#         queue.appendleft((cur_node*2, cur_time))

#     for i in [-1, 1]:
#         if cur_node+i < 0 or cur_node+i > 100050 or visited[cur_node+i]:
#             continue
#         else:
#             visited[cur_node+i] = True
#             queue.append((cur_node+i, cur_time+1))

# 다익스트라 풀이
import heapq

N, K = list(map(int, input().split()))
visited = [False] * 200110
dist = [float('inf')] * 200110

def bfs():
    queue = [(0, N)]
    dist[N] = 0
    
    while queue:
        _, cur_node = heapq.heappop(queue)
        if cur_node == K:
            return dist[cur_node]
        
        for next_node, weight in [(cur_node+1, 1), (cur_node-1, 1), (cur_node*2, 0)]:
            if next_node<0 or next_node>100050:
                continue
            if visited[next_node]:
                continue
            
            if dist[cur_node] + weight < dist[next_node]:
                dist[next_node] = dist[cur_node] + weight
                heapq.heappush(queue, (dist[next_node], next_node))
        visited[cur_node] = True

print(bfs())

# https://velog.io/@iamdudumon/0-1-BFS
