'''
Level: G5
Time: 37m47s
'''
import sys
input = lambda: sys.stdin.readline().strip()

if __name__ == "__main__":
    N = int(input())
    
    sign = [''] * (N+1)
    sign[1] = "+"
    for i in range(N-1):
        sys.stdout.write(f"? {i+1} * {i+2}\n")
        sys.stdout.flush()
        result = input()
        if result == "+":
            sign[i+2] = sign[i+1]
        else:
            sign[i+2] = "-" if sign[i+1]=='+' else '+'
        
    for i in range(2, N+1):
        if sign[1] == sign[i]:
            sys.stdout.write(f"? {1} + {i}\n")
            sys.stdout.flush()
            result = input()
            if result == "+":
                flag = False
            else:
                flag = True
            break
    else:
        sys.stdout.write(f"? {2} + {3}\n")
        sys.stdout.flush()
        result = input()
        if result == "-":
            flag = False
        else:
            flag = True
        

    sys.stdout.write("! ")
    for i in range(1, N+1):
        if flag:
            sys.stdout.write(f'{"+" if sign[i]=="-" else "-"} ')
        else:
            sys.stdout.write(f"{sign[i]} ")
    sys.stdout.write("\n")
    sys.stdout.flush()
            
