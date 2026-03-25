"""
进程之间不共享全局变量
    每个进程拥有独立的内存空间，子进程会复制父进程的全局变量到自己的内存空间中，修改子进程的全局变量
    不会影响父进程或其他子进程
"""
import multiprocessing
import time

# 全局变量
global_var = 100


def modify_var():
    global global_var
    print(f"子进程启动前，global_var = {global_var}")
    global_var = 200  # 修改全局变量
    print(f"子进程修改后，global_var = {global_var}")


if __name__ == "__main__":
    print(f"父进程启动前，global_var = {global_var}")

    p = multiprocessing.Process(target=modify_var)
    p.start()
    p.join() # 阻塞主进程，等待子进程结束

    print(f"父进程结束后，global_var = {global_var}")  # 仍然是 100