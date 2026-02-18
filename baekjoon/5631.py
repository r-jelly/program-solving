'''
Level: G4
Time: 1h15m04s
'''
import sys
input = lambda: sys.stdin.readline().strip()


def get_inner(dist, radius_pow_2):
    left, right = 0, len(dist)-1
    
    while left <= right:
        mid = (left + right) // 2
        if radius_pow_2 >= dist[mid]:
            # 원하는 값이 나와도 바로 반환시키면 안됨! -> 중복된 값이 여러 개 등장할 수도 있으므로
            # Upper Bound를 찾기 위해서 계속 더해주기!
            left = mid+1
        else:
            right = mid-1

    return left


def get_distance(houses, x, y):
    return [(hx-x)**2 + (hy-y)**2 for hx, hy in houses]


if __name__ == "__main__":
    for i in range(4):
        N = int(input())
        if N == 0:
            break

        houses = [list(map(int, input().split())) for _ in range(N)]
        ax, ay, bx, by, q = list(map(int, input().split()))
        radius = [list(map(int, input().split())) for _ in range(q)]

        dist_a = sorted(get_distance(houses, ax, ay))
        dist_b = sorted(get_distance(houses, bx, by))

        print(f"Case {i+1}:")
        for ra, rb in radius:
            count = max(0, N - get_inner(dist_a, ra**2) - get_inner(dist_b, rb**2))
            print(count)