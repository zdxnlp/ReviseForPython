def solution():
    s = list(input().strip())
    t = {}
    for i in range(len(s)):
        char = s[i]
        if char not in t:
            # 第一次出现：初始化首尾索引都为i
            t[char] = [i, i]
        else:
            # 非第一次出现：仅更新末尾索引
            t[char][1] = i
    v = []
    # 进行区间合并
    for key in t:
        v.append(t[key])
    cur = v[0]
    res = []
    for i in range(1, len(v)):
        if v[i][0] <= cur[1]:
            cur[0] = min(cur[0], v[i][0])
            cur[1] = max(cur[1], v[i][1])
        else:
            res.append(cur[1]-cur[0]+1)
            cur = v[i]
    res.append(cur[1]-cur[0]+1)
    print(res)

if __name__ == '__main__':
    solution()