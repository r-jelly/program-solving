import sys
N, M = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))


def dfs(nums, visited, stack=[]):
    if len(stack) == M:
        return [stack[:]]
    
    num_seq = []
    for i, num in enumerate(nums):
        if visited[i]:
            continue

        visited[i] = True
        stack.append(num)
        num_seq += dfs(nums, visited, stack)[:]
        visited[i] = False
        stack.pop()

    return num_seq

visited = [False] * N
num_seqs = []
for i, num in enumerate(num_list):
    visited[i] = True
    cur_seqs = dfs(num_list, visited, [num])
    num_seqs.extend(cur_seqs)
    visited[i] = False

for num_seq in sorted(num_seqs):
    for num in num_seq:
        sys.stdout.write(str(num)+" ")
    sys.stdout.write("\n")

# Solved 18m49s