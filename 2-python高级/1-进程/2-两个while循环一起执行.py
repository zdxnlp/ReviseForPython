from multiprocessing import Process
import time

def run_proc():
    """子进程要执行的代码"""
    while True:
        print('--2--')
        time.sleep(1)

if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    while True:
        print('--1--')
        time.sleep(1)

# 创建子进层时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
# 孤儿进程：父进程退出（kill杀死父进程），子进程变成孤儿
# 僵尸进程：子进程退出，父进程在忙碌，没有回收它，要避免僵尸。python进程变为僵尸进程后，名字会改变