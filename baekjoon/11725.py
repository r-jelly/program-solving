# from collections import deque
# N = int(input())

# tree = dict()
# for i in range(N-1):
#     node1, node2 = list(map(int, input().split()))
#     if node1 not in tree:
#         tree[node1] = []
#     if node2 not in tree:
#         tree[node2] = []
#     tree[node1].append(node2)
#     tree[node2].append(node1)

# result = [None] * (N+1)
# queue = deque([1])
# visited = [False]*(N+1)
# while queue:
#     cur_node = queue.popleft()
#     visited[cur_node] = True

#     for node in tree[cur_node]:
#         if visited[node]:
#             continue
#         result[node] = cur_node
#         queue.append(node)

# for i in range(2, N+1):
#     print(result[i])

from collections import deque
import sys

N = int(sys.stdin.readline())
tree = dict()

for i in range(N-1):
    node1, node2 = list(map(int, sys.stdin.readline().split()))
    tree[node1] = tree.get(node1, list()) + [node2]
    tree[node2] = tree.get(node2, list()) + [node1]

result = [None, 1] + [None] * (N)
queue = deque([1])

while queue:
    cur_node = queue.popleft()
    for node in tree[cur_node]:
        if result[node] != None:
            continue
        result[node] = cur_node
        queue.append(node)

for i in range(2, N+1):
    print(result[i])