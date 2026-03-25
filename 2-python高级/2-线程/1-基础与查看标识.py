# 线程是Python开发中 IO 密集型任务并发处理的核心工具，
# 也是web服务器、接口调用、数据库操作、文件读写等高频场景的性能优化核心手段。
"""
线程：CPU调度和执行的最小单位，也叫轻量级进程。线程必须依附于进程存在，同一个进程内的所有线程
    共享该进程的内存空间、文件句柄等系统资源，线程自身仅保留极少的运行必需资源（栈、程序计数器等）
线程的核心适用场景：web接口请求、数据库/Redis操作、文件批量读写、爬虫、日志异步写入等绝大多数IO密集业务
"""

# 查看进程与线程标识

import threading
import os
import time

def thread_task():
    # 查看当前线程信息、所属进程ID
    current_thread = threading.current_thread()
    print(f"线程名：{current_thread}，线程ID：{current_thread.ident}，所属进程ID：{os.getpid()}")
    time.sleep(1)
    print(f'{current_thread}执行结束')

if __name__ == '__main__':
    print(f"主线程名：{threading.main_thread().name}，主线程ID：{threading.main_thread().ident}，进程ID：{os.getpid()}")
    print("-" * 50)

    # 创建2个子线程
    t1 = threading.Thread(target=thread_task, name="工作线程1")
    t2 = threading.Thread(target=thread_task, name="工作线程2")

    # 启动线程
    t1.start()
    t2.start()
