N, K = list(map(int, input().split()))

item_list = []
for i in range(N):
    W, V = list(map(int, input().split()))
    item_list.append((W, V))
# item_list.sort(key=lambda x: x[0])
# item_list.sort(key=lambda x: x[1], reverse=True)

# max_value = 0
# for i in range(N):
#     cur_value = 0
#     cur_weight = 0
#     for j in range(i, N):
#         if cur_weight + item_list[j][0] > K:
#             continue
#         cur_weight += item_list[j][0]
#         cur_value += item_list[j][1]

#     if max_value < cur_value:
#         max_value = cur_value

# print(max_value)

dp = [[0]*(K+1) for _ in range(N)]
for i in range(N):
    w, v = item_list[i]
    dp[i][w] = v
    