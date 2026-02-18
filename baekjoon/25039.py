'''
Level: S3
Time: 35m39s
'''

import sys
input = sys.stdin.readline

def solution(N, beekeepers):
    sorted_beekeepers = sorted(beekeepers, key=lambda x: (-x[2], x[1]))
    ranks = [[0, 0] for _ in range(N)]
    
    for i, (idx, name, cur_p) in enumerate(sorted_beekeepers):
        ranks[idx] = [i+1, N]
        for j in range(i+1):
            if cur_p+500 > sorted_beekeepers[j][2]:
                ranks[idx][0] = j+1
                break
            elif cur_p+500 == sorted_beekeepers[j][2]:
                if name < sorted_beekeepers[j][1]:
                    ranks[idx][0] = j+1
                    break
        for j in range(i+1, N):
            if cur_p-500 > sorted_beekeepers[j][2]:
                ranks[idx][1] = j
                break
            elif cur_p-500 == sorted_beekeepers[j][2]:
                if name < sorted_beekeepers[j][1]:
                    ranks[idx][1] = j
                    break
    return ranks


if __name__ == "__main__":
    N = int(input())
    beekeepers = []

    for i in range(N):
        name, *nums = input().strip().split()
        beekeepers.append((i, name, sum(map(int, nums))))

    ranks = solution(N, beekeepers)
    for rank in ranks:
        print(*rank)
