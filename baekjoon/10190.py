'''
Level: S5
Time: 10m32s
'''
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        acronym, M = input().split()
        print(acronym)

        for _ in range(int(M)):
            words = input().split()
            cur_acronym = ''.join([word[0] for word in words])
            if cur_acronym == acronym:
                print(' '.join(words))