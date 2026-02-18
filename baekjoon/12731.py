'''
Level: G5
Time: 1h16m18s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(T, a_to_b, b_to_a):
    if not a_to_b:
        return 0, len(b_to_a)
    elif not b_to_a:
        return len(a_to_b), 0

    start_a, start_b = 0, 0

    b_idx = 0
    for _, time_b in sorted(a_to_b, key=lambda x: x[1]):
        H, M = list(map(int, time_b.split(":")))
        M += T
        if M >= 60:
            H += 1
            M -= 60
        next_move_time = f"{H:02d}:{M:02d}"

        while b_idx < len(b_to_a):
            if b_to_a[b_idx][0] < next_move_time:
                start_b += 1
                b_idx += 1
            else:
                b_idx += 1
                break
    start_b += len(b_to_a) - b_idx

    a_idx = 0
    for _, time_a in sorted(b_to_a, key=lambda x: x[1]):
        H, M = list(map(int, time_a.split(":")))
        M += T 
        if M >= 60:
            H += 1
            M -= 60
        next_move_time = f"{H:02d}:{M:02d}"

        while a_idx < len(a_to_b):
            if a_to_b[a_idx][0] < next_move_time:
                start_a += 1
                a_idx += 1
            else:
                a_idx += 1
                break
    start_a += len(a_to_b) - a_idx

    return start_a, start_b

if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        T = int(input())
        num_a, num_b = list(map(int, input().split()))
        a_to_b = sorted([input().split() for _ in range(num_a)])
        b_to_a = sorted([input().split() for _ in range(num_b)])

        print(f"Case #{i+1}:", *solution(T, a_to_b, b_to_a))
