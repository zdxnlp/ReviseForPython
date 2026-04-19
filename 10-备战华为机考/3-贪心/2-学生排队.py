import sys
from collections import Counter

def main():
    # 读取输入，处理ACM标准输入
    input_line = sys.stdin.readline().strip()
    nums = list(map(int, input_line.split()))
    num_count = Counter(nums)
    total_len = len(nums)
    k = total_len // 2  # 每个队需要的长度

    # 无解判断：有数字出现次数超过2
    for num, cnt in num_count.items():
        if cnt > 2:
            print("null")
            return

    # 拆分必选列表（出现2次）和可选列表（出现1次）
    must_include = []
    optional = []
    for num, cnt in num_count.items():
        if cnt == 2:
            must_include.append(num)
        else:
            optional.append(num)

    # 计算需要从可选列表中选的数量
    need_select = k - len(must_include)
    # 对可选列表排序，选最小的need_select个放入n1，保证n1和最小
    optional_sorted = sorted(optional)

    # 构造两队并排序
    n1 = sorted(must_include + optional_sorted[:need_select])
    n2 = sorted(must_include + optional_sorted[need_select:])

    # 输出结果
    print(' '.join(map(str, n1)))
    print(' '.join(map(str, n2)))

if __name__ == "__main__":
    main()