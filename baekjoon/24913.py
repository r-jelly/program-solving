'''
Level: S2
Time: 50m57s
'''
import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()


if __name__ == "__main__":
    N, Q = list(map(int, input().split()))
    vote_dict = defaultdict(int)
    vote_jh, vote_not_jh = 0, 0
    cur_max = 0
    for _ in range(Q):
        cmd, x, y = list(map(int, input().split()))

        if cmd == 1:
            if y <= N:
                vote_dict[y] += x
                vote_not_jh += x
                cur_max = max(cur_max, vote_dict[y])
            elif y == N+1:
                vote_jh += x

        elif cmd == 2:
            expected_jh = vote_jh + x
            # if not vote_dict:
            #     if expected_jh > y:
            #         sys.stdout.write("YES\n")
            #     else:
            #         sys.stdout.write("NO\n")
                    
            if (vote_not_jh+y) > (expected_jh-1)*N:
                sys.stdout.write("NO\n")
            else:
                if cur_max >= expected_jh:
                    sys.stdout.write("NO\n")
                else:
                    sys.stdout.write("YES\n")