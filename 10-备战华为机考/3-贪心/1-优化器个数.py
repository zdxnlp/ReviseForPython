# 1 1 _
# _ 1 1 1 _
# _ 1 1
# 大于3的方式中，上面三种一定不能使得所有被优化，返回-1

# 1 + 1 返回-1
# 2 + 1 1 返回-1

def solve():
    n = int(input())
    pos = list(map(int, input().split()))
    res = 0
    if n==1 and pos[0]==1:
        return -1
    elif n==2 and pos[0]==1 and pos[1]==1:
        return -1
    else:
        if pos[0]==1 and pos[1]==1:
            return -1
        elif pos[-1]==1 and pos[-2]==1:
            return -1

    return res

if __name__ == '__main__':
    print(solve())