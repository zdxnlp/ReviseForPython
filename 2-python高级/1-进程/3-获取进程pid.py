from multiprocessing import Process
import time
import os

def run_proc():
    """子进程要执行的代码"""
    print('子进程运行中，pid=%d...'%os.getpid())
    print('子进程将要结束...')

if __name__ == '__main__':
    print('父进程运行中，pid=%d...'%os.getpid())
    p = Process(target=run_proc)
    p.start()

"""
    获取父亲的pid
    os.getppid()
    进程组 方便管理进程
    kill -9 -3811 可以直接杀掉某一个进程组。孩子没结束，父亲会一直等
"""