'''
Level: S3
Time: 27m56s
'''
def solution(scores):
    dp = [[0, 0]] * len(scores)
    dp[1] = [scores[1], scores[1]]

    for i in range(2, len(scores)):
        dp[i] = [
            max(dp[i-2][0], dp[i-1][1]) + scores[i],
            max(dp[i-2]) + scores[i]
        ]
    return max(dp[-1])
    
def solution_optimal(scores):
    if len(scores) <= 3:
        return sum(scores)
    
    dp = [0] * len(scores)
    dp[1] = scores[1]
    dp[2] = dp[1]+scores[2]
    for i in range(3, len(scores)):
        dp[i] = max(
            dp[i-3] + scores[i-1],
            dp[i-2]
        ) + scores[i]
    return dp[-1]

if __name__ == "__main__":
    N = int(input())

    scores = [0]
    for _ in range(N):
        score = int(input())
        scores.append(score)

    print(solution(scores))