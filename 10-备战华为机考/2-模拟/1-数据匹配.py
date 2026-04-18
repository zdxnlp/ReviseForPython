def solve():
    data = input().split()
    target = data[0]
    target_len = len(target)
    candidate = data[1:]
    un_match_dict = {}
    match_dict = {}
    for i in range(0, len(candidate)):
        if len(candidate[i]) > target_len or un_match_dict.get(candidate[i]): # 长度大于目标字符串，不匹配
            un_match_dict.update({candidate[i]:1})
        elif match_dict.get(candidate[i]):
            match_dict[candidate[i]] += 1
        else:
            for j in range(len(candidate[i])):
                if candidate[i][j] != target[j]:
                    if candidate[i] not in un_match_dict.keys():
                        un_match_dict[candidate[i]] = 1
                    else:
                        un_match_dict[candidate[i]] += 1
                    break
                if j==len(candidate[i])-1:
                    if candidate[i] not in match_dict.keys():
                        match_dict[candidate[i]] = 1
                    else:
                        match_dict[candidate[i]] += 1
    print(match_dict)



if __name__ == '__main__':
    solve()