'''
Level: S2
Time: 39m03s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(num, lengths):

    # for l in reversed(range(1 if num>len(lengths) else lengths[-num], lengths[-1]+1)):
    #     count = 0
    #     for length in reversed(lengths):
    #         count += length//l
    #     if count >= num:
    #         return l

    left, right = 1, lengths[-1]
    answer = 0
    while left <= right:
        mid = (left+right) // 2
        count = sum(length//mid for length in lengths)

        if count >= M:
            answer = mid
            left = mid+1
        else:
            right = mid-1
    return answer

if __name__ == "__main__":
    M, N = list(map(int, input().split()))
    lengths = sorted(list(map(int, input().split())))
    print(solution(M, lengths))