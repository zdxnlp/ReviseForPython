# 当任务量巨大时，手动管理进程太麻烦，需要使用进程池自动调度。
"""
1. Pool(processes=N):定义一个包含N个进程的池子
2. .map(func,iterable):同步执行，将可迭代对象分发给进程，阻塞直到结果返回
3. .apply_async(func,args):异步执行，提交一个任务，返回一个Future对象
"""
# 常用于批量处理图片、生成报表、数据清洗等
import multiprocessing
import os

def work_task(file_name):
    """模拟处理一个文件"""
    # 业务逻辑
    print(f'进程{os.getpid()}正在处理：{file_name}')
    return f'完成：{file_name}'

if __name__ == '__main__':
    # 假设有10个任务需要处理
    tasks = [f'file_{i}.txt' for i in range(10)]

    # 创建进程池，默认大小为CPU核心数
    with multiprocessing.Pool(3) as pool:
        # 使用map分发任务
        res = pool.map(work_task, tasks)

    print('所有任务处理完毕：')
    for i in res:
        print(i)