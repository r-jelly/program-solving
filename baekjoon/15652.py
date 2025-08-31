'''
Level: S3
Time: 07m18s
'''

N, M = list(map(int, input().split()))

def dfs(node: int, seq: list, length: int):
    if length == M:
        print(*seq)
        return
    
    for i in range(node, N+1):
        seq.append(i)
        dfs(i, seq, length+1)
        seq.pop()
    return

dfs(1, [], 0)