'''
Level: S5
Time: 19m39s
'''
import sys
input = lambda: sys.stdin.readline().strip()


if __name__ == "__main__":
    N = int(input())
    y_score = 0
    for _ in range(N):
        S, A, T, M = list(map(float, input().split()))
        y_score += S * (1+A) * (T+M) / (T*A)
    y_score = round(y_score, 3)

    scores = [y_score]
    P = int(input())
    for _ in range(P):
        score = float(input())
        scores.append(score * 4)

    scores = sorted(scores, reverse=True)
    rank = scores.index(y_score) + 1
    if rank <= len(scores) * 0.15:
        print(f'The total score of Younghoon "The God" is {y_score/4:.2f}.')
    else:
        print(f'The total score of Younghoon is {y_score/4:.2f}.')