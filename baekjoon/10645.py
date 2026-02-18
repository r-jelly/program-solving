'''
Level: S2
Time: 25m09s
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    
    row, col = defaultdict(list), defaultdict(list)
    rdiag, ldiag = defaultdict(list), defaultdict(list)
    answer = -1
    for i in range(N):
        x, y = list(map(int, input().split()))
        row[x].append(i+1)
        col[y].append(i+1)
        rdiag[x-y].append(i+1)
        ldiag[x+y].append(i+1)

        if answer == -1 and len(row[x]) >= K:
            answer = i+1
        if answer == -1 and len(col[y]) >= K:
            answer = i+1
        if answer == -1 and len(rdiag[x-y]) >= K:
            answer = i+1
        if answer == -1 and len(ldiag[x+y]) >= K:
            answer = i+1
        
    print(answer)
