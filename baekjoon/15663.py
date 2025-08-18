import sys

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))

visited = [False]*N
seq     = set()
stack   = list()

nums.sort()

def dfs(cur_seq, length=0):
    if length == M:
        if '-'.join(cur_seq) not in seq:
            seq.add('-'.join(cur_seq))
            for i in cur_seq:
                sys.stdout.write(str(i)+" ")
            sys.stdout.write("\n")
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        cur_seq.append(str(nums[i]))
        dfs(cur_seq[:], length+1)
        visited[i] = False
        cur_seq.pop()

dfs(stack, 0)