
def solution():
    pos = None
    n = int(input())
    b = list(map(int, input().split()))
    v = int(input())
    div = 0
    while div < n-1:
        if b[div+1] < b[div]:
            break
        div += 1

    def insert_pos(i,j,value):
        position = None
        while i<=j:
            if value <= b[i]:
                position = i
                break
            i += 1
        if position is None:
            return j+1
        else:
            return position

    if div == n-1: # 表示原本的数列就是严格非递减序列，直接将v插入合适的位置就行
        pos = insert_pos(0,n-1,v)
    else: # 表示原来的序列先分为了两部分
        l1 = 0 # 第一个序列的第一个值
        r1 = div # 第一个序列的最后一个值
        l2 = div+1 # 第二个序列的第一个值
        r2 = -1 # 第二个序列的最后一个值
        if v < b[r2]:
            pos = insert_pos(l2,r2,v) + l2
        else:
            pos = insert_pos(l1,r1,v)
    print(pos)

    if pos == 0:
        print(v,end=' ')
        for i in range(n):
            if i == n-1:
                print(b[i])
            else:
                print(b[i], end=' ')
    elif pos == n:
        for i in range(n):
            print(b[i],end=' ')
        print(v)
    else:
        for i in range(n):
            if pos == i:
                print(v,end=' ')
                print(b[i],end=' ')
            elif i == n-1:
                print(b[i])
            else:
                print(b[i],end=' ')


def main():
    # 读取输入
    n = int(input())
    boards = list(map(int, input().split()))
    new_len = int(input())

    # 步骤1：找到数组的峰值位置（最大值的下标）
    peak_idx = 0
    while peak_idx < n - 1:
        if boards[peak_idx + 1] < boards[peak_idx]:
            break
        peak_idx += 1

    # 步骤2：预处理段B的最大值（用于判断段A开头插入的合法性）
    max_B = -1
    if peak_idx < n - 1:
        max_B = max(boards[peak_idx + 1:])
    a0 = boards[0]  # 段A的第一个元素

    # 步骤3：优先找段A的最小合法插入位置（下标更小，优先遍历）
    insert_pos = -1
    # 段A的插入位置范围：0 ~ peak_idx+1
    for pos in range(0, peak_idx + 2):
        # 检查插入后段A是否仍非递减
        valid = True
        if pos > 0:
            if new_len < boards[pos - 1]:
                valid = False
        if pos <= peak_idx:
            if new_len > boards[pos]:
                valid = False
        # 插入到段A开头，需要满足new_len >= 段B的所有元素
        if pos == 0 and peak_idx < n - 1:
            if new_len < max_B:
                valid = False
        if valid:
            insert_pos = pos
            break

    # 步骤4：段A无合法位置，找段B的最小合法插入位置
    if insert_pos == -1:
        # 段B的插入位置范围：peak_idx+1 ~ n
        for pos in range(peak_idx + 1, n + 1):
            # 检查插入后段B是否仍非递减
            valid = True
            if pos > peak_idx + 1:
                if new_len < boards[pos - 1]:
                    valid = False
            if pos <= n - 1:
                if new_len > boards[pos]:
                    valid = False
            # 段B的元素必须<=段A的第一个元素
            if new_len > a0:
                valid = False
            if valid:
                insert_pos = pos
                break

    # 步骤5：插入新元素，输出结果
    result = boards[:insert_pos] + [new_len] + boards[insert_pos:]
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()