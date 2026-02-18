import sys
input = lambda: sys.stdin.readline().strip()

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    outter_product = (x2-x1)*(y3-y2) - (y2-y1)*(x3-x2)
    if outter_product > 0:
        return 1
    elif outter_product < 0:
        return -1
    else:
        return 0
    
if __name__ == "__main__":
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, x4, y4 = list(map(int, input().split()))
    
    p1p2 = ccw((x1, y1), (x2, y2), (x3, y3)) * ccw((x1, y1), (x2, y2), (x4, y4))
    p3p4 = ccw((x3, y3), (x4, y4), (x1, y1)) * ccw((x3, y3), (x4, y4), (x2, y2))
    
    if p1p2==0 and p3p4==0:
        print(int(max(x1, x2)<=min(x3, x4) and min(x1, x2)<=max(x3, x4)))
    else:
        print(int(p1p2<=0 and p3p4<=0))
