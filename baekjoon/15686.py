'''
Level: G5
Time: 1h02m05s
'''

import sys
input = sys.stdin.readline


def find_point(board, N):
    house_list, shop_list = [], []
    for i in range(N):
        for j in range(N):
            if board[i][j] == "1":
                house_list.append((i, j))
            elif board[i][j] == "2":
                shop_list.append((i, j))
    return (house_list, shop_list)


def calc_dist(house_list, shop_list):
    all_dist = 0
    for hx, hy in house_list:
        cur_dist = float('inf')
        for sx, sy in shop_list:
            cur_dist = min(cur_dist, abs(sy-hy)+abs(sx-hx))
        all_dist += cur_dist
    return all_dist


def dfs(house_list, shop_list, select_shop_list, cur_dist, cur_idx, M):
    if len(select_shop_list) == M:
        return min(cur_dist, calc_dist(house_list, select_shop_list))
    
    dist = float('inf')
    for i in range(cur_idx+1, len(shop_list)):
        select_shop_list.append(shop_list[i])
        dist = min(dist, dfs(house_list, shop_list, select_shop_list, cur_dist, i, M))
        select_shop_list.pop()
    return dist


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    
    cur_shop_num, board = 0, []
    for _ in range(N):
        line = input().split()
        cur_shop_num += line.count("2")
        board.append(line)

    house_list, shop_list = find_point(board, N)
    print(dfs(house_list, shop_list, [], float('inf'), -1, M))
