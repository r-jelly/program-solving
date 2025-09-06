'''
Level: S3
Time: 21m50s
'''

from collections import deque
import sys

S = input()

deq = deque([])
flag = False
for s in S:
    if s=="<":
        flag = True
        while deq:
            sys.stdout.write(deq.pop())
        sys.stdout.write(s)
    elif s==">":
        flag = False
        sys.stdout.write(s)
    else:
        if flag:
            sys.stdout.write(s)
        else:
            if s==" ":
                while deq:
                    sys.stdout.write(deq.pop())
                sys.stdout.write(" ")
            else:
                deq.append(s)

while deq:
    sys.stdout.write(deq.pop())