# 0-1 Knapsack Algorithm

N, K = list(map(int, input().split()))

item_list = []
for i in range(N):
    W, V = list(map(int, input().split()))
    item_list.append((W, V))

# dp[item][weight]

dp = [[0]*(K+1) for _ in range(N+1)]
for item_idx in range(N):
    for weight in range(K+1):
        if item_list[item_idx][0] <= weight:
            dp[item_idx+1][weight] = max(
                dp[item_idx][weight],
                dp[item_idx][weight - item_list[item_idx][0]] + item_list[item_idx][1]
            )
        else:
            dp[item_idx+1][weight] = dp[item_idx][weight]

print(dp[-1][-1])