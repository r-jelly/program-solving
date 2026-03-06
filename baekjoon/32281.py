'''
Level: S5
Time: 18m20s
'''
def solution(glass_count: list[int]):
    answer = 0
    for count in glass_count:
        answer += (count)*(count+1)//2
    return answer

if __name__ == "__main__":
    N = int(input())
    y_0 = input()

    continuous_glass_count = []
    count = 0
    for glass in y_0:
        if '1' == glass:
            count += 1
        else:
            if count != 0:
                continuous_glass_count.append(count)
                count = 0
    else:
        if count:
            continuous_glass_count.append(count)

    print(solution(continuous_glass_count))