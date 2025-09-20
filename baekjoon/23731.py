'''
Level: S4
Time: 22m46s
'''

N = int(input())

multi = 10
for _ in range(len(str(N))):
    upper = N // multi
    cur_digit = (N%multi) // (multi//10)

    if cur_digit >= 5:
        N = (upper+1) * multi
    multi *= 10

print(N)