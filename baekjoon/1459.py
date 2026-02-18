'''
Level: S3
Time: 26m47s
'''
import sys
input = lambda: sys.stdin.readline().strip()

if __name__ == "__main__":
    x, y, w, s = list(map(int, input().split()))

    long_side, short_side = max(x, y), min(x, y)
    if w*2 < s:
        answer = w * (long_side+short_side)
    elif w < s:
        answer = s * short_side + w * (long_side-short_side)
    else:
        if (long_side-short_side)%2==0:
            answer = s * long_side
        else:
            answer = s * (long_side-1) + w
    print(answer)