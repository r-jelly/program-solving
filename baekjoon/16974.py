'''
Level: G5
Time: 1h04m40s
'''
import sys
input = lambda: sys.stdin.readline().strip()


def get_num_patty(dp, level, X):
    if X <= level:
        return 0
    if level == 0:
        return 1

    if X <= dp[level-1][0] + 1:
        return get_num_patty(dp, level-1, X-1)
    else:
        return 1 + dp[level-1][1] + get_num_patty(dp, level-1, X-dp[level-1][0]-2)


def solution(N, X):
    '''
    Args:
        N: 햄버거의 레벨 (1<=N<=50)
        X: 아래부터 먹은 레이어의 수 (1<=X<=(N레벨의 총 레이어 수))
    Return:
        answer: X 레이어 중 패티의 수
    '''
    dp = [[] for _ in range(N+1)] # [총 길이, 현재 레벨의 총 패티 수]
    dp[0] = [1, 1]
    
    for i in range(1, N+1):
        num_prev_layer, num_prev_patty = dp[i-1]
        dp[i] = [num_prev_layer*2 + 3, num_prev_patty*2 + 1]

    answer = get_num_patty(dp, N, X)
    return answer


if __name__ == "__main__":
    N, X = list(map(int, input().split()))
    print(solution(N, X))