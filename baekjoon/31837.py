'''
Level: G4
Time: 27m59s
'''
import sys
input = sys.stdin.readline

def check_duplicate(time_table, start_time, end_time):
    for prev_start_time, prev_end_time in time_table:
        if not prev_start_time:
            continue
        if start_time<=prev_start_time<end_time:
            return True
        elif start_time<prev_end_time<=end_time:
            return True
        elif prev_start_time<start_time and end_time<prev_end_time:
            return True
    return False


def dfs(groups, cur_group_idx, cur_credit, time_table):
    if cur_group_idx == len(groups):
        return cur_credit == 22
    
    answer = 0
    for credit, date, start_time, end_time in groups[cur_group_idx]:
        credit, date = int(credit), int(date)
        if start_time and end_time:
            if check_duplicate(time_table[date], start_time, end_time):
                continue
            
        time_table[date].append([start_time, end_time])
        answer += dfs(groups, cur_group_idx+1, cur_credit+credit, time_table)
        time_table[date].pop()

    return answer
        
    
if __name__ == "__main__":
    N = int(input())
    groups = []
    for _ in range(N):
        classes = [[0, 0, None, None]]
        A = int(input())
        for _ in range(A):
            classes.append(input().strip().split())
        groups.append(classes)

    time_table = [[] for _ in range(10)]
    print(dfs(groups, 0, 0, time_table))