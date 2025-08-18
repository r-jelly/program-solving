A, B, C = list(map(int, input().split()))

def new_pow(x, y, z):
    '''
    calculate x**y mod z
    '''
    if y==1:
        return x%z
    elif y==2:
        return (x*x)%z

    x_part = new_pow(x, y>>1, z)

    if y%2:
        return (x%z * x_part * x_part) % z
    else:
        return (x_part * x_part) % z


print(new_pow(A, B, C))