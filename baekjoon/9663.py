# def dfs(board, N, cur_row, queens):
#     if len(queens) == N:
#         return [queens]

#     can_queen = []
#     for x in range(N):
#         if not board[cur_row][x]:
#             if cur_row == N-1:
#                 return [queens+[(x, cur_row)]]
            
#             new_board = [arr[:] for arr in board]
#             new_board[cur_row][x] = True
#             new_board = check_queen(new_board, N, x, cur_row)
#             if all(new_board[cur_row+1]):
#                 continue

#             result = dfs(new_board, N, cur_row+1, queens+[(x, cur_row)])
#             if result:
#                 can_queen.extend(result)

#     return can_queen
                


# def check_queen(board, N, x, y):
#     for i in range(N):
#         board[y][i] = True
#         board[i][x] = True
            
#     for i in range(N):
#         if 0 <= (y-x+i) < N:
#             board[y-(x-i)][i] = True
#         if 0 <= (y+x-i) < N:
#             board[y+x-i][i] = True
#     return board
#####
# def dfs(N, cur_row, queens_col):
#     if cur_row >= N:
#         return [queens_col]
    
#     can_queen = []
#     for i in range(N):
#         if i in queens_col:
#             continue
#         elif check_diag(cur_row, i, queens_col):
#             result = dfs(N, cur_row+1, queens_col+[i])
#             if result:
#                 can_queen.extend(result)
#     return can_queen

# def check_diag(cur_row, cur_col, queens_col):
#     for row, col in enumerate(queens_col):
#         if abs(row-cur_row) == abs(col-cur_col):
#             return False
#     return True

# N = int(input())
# can_queen = []

# for col in range(N):
#     can_queen.extend(dfs(N, 1, [col]))

# print(len(can_queen))
################
# N = int(input())
# cols = [0]*N

# def dfs(N, cur_row):
#     if N == cur_row:
#         return 1
    
#     cnt = 0
#     for i in range(N):
#         cols[cur_row] = i
#         if check_queen(cur_row):
#             cnt += dfs(N, cur_row+1)

#     return cnt

# def check_queen(cur_row):
#     for i in range(cur_row):
#         if cols[cur_row] == cols[i]:
#             return False
#         elif abs(cols[cur_row]-cols[i]) == abs(cur_row-i):
#             return False
#     return True

# print(dfs(N, 0))


N = int(input())
cols = [False] * N
left_diag = [False] * (N*2) # 오른쪽 아래에서 왼쪽 위로, row+col 값 동일
right_diag = [False] * (N*2) # 왼쪽 아래에서 오른쪽 위로, row-col 값 동일

def dfs(N, cur_row):
    if N==cur_row:
        return 1
    
    cnt = 0
    for col in range(N):
        if not cols[col] and not left_diag[cur_row+col] and not right_diag[cur_row-col]:
            cols[col] = True
            left_diag[cur_row+col] = True
            right_diag[cur_row-col] = True

            cnt += dfs(N, cur_row+1)

            cols[col] = False
            left_diag[cur_row+col] = False
            right_diag[cur_row-col] = False

    return cnt

print(dfs(N, 0))